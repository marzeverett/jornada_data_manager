
import pickle
import os
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd 

#https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/
#https://plotly.com/python/figure-labels/
#Help for multiple lines: https://www.tutorialspoint.com/how-to-plot-multiple-lines-on-the-same-y-axis-in-python-plotly 
#Numpy indexing: https://stackoverflow.com/questions/42916029/indexing-over-the-last-axis-when-you-dont-know-the-rank-in-advance

#Experiment folder path 
def get_full_experiment_folder(experiment_object):
    full_path = experiment_object["experiment_folder_path"] + experiment_object["experiment_name"] +"/" +experiment_object["dataset_name"]+"/"
    return full_path

#CHANGE is here 
def unnormalize_data_transformation(feature_array, dataset_descriptor):
    y_columns = dataset_descriptor["y_columns"]
    reverse_mapping = dataset_descriptor["reverse_mapping"]
    normalization_data = dataset_descriptor["normalization_data"]
    norm_keys = list(normalization_data.keys())
    #For each feature in our feature vector:
    for i in range(0, len(feature_array)):
        name = y_columns[i]
        #mapped_item = reverse_mapping[name]
        #if mapped_item in list(normalization_data.keys()):
        if name in list(normalization_data.keys()):
            #feature_info = normalization_data[mapped_item]
            feature_info = normalization_data[name]
            max_val = feature_info["max"]
            min_val = feature_info["min"]
            feature_array[i] = (feature_array[i]*(max_val-min_val))+min_val

#Unnormalize data 
#This was a confusing way to do it, Marz. 
def unnormalize_data(dataset_descriptor, dataset_result, experiment_result):
    y_map = {
        "y": "y_unnormalized",
        "y_train": "y_train_unnormalized",
        "y_test": "y_test_unnormalized"
    }
    x_pred_map = {
        "x": "x_pred_unnormalized",
        "x_train": "x_pred_train_unnormalized",
        "x_test": "x_pred_test_unnormalized"
    }
    for y_key in list(y_map.keys()): 
        y_vals = dataset_result[y_key].copy()
        np.apply_along_axis(unnormalize_data_transformation, -1, y_vals, dataset_descriptor)
        #Map it
        dataset_result[y_map[y_key]] = y_vals
    for x_key in list(x_pred_map.keys()): 
        y_vals = experiment_result["predictions"][x_key].copy()
        np.apply_along_axis(unnormalize_data_transformation, -1, y_vals, dataset_descriptor)
        #Map it
        experiment_result["predictions"][x_pred_map[x_key]] = y_vals

# #y columns will either be 2D or 3D. 
#Going to have to think about how we visualize 
#predictions for y with more than one output! 
def plot_model_training_history(experiment_descriptor, experiment_result, metric, val=True):
    history = experiment_result["model_history"]
    title = metric+ " across training epochs"
    title = title.title()
    fig = go.Figure()
    y_vals = history[metric]
    x_vals = list(range(0, len(y_vals), 1))
    fig.add_trace(go.Scatter(x=x_vals, y=y_vals, name=metric, mode="lines"))
    if val:
        val_metric = "val_"+metric
        fig.add_trace(go.Scatter(x=x_vals, y=history[val_metric], name=val_metric, mode="lines"))
    fig.update_layout(
        title=title,
        xaxis_title="Epochs",
        yaxis_title=f"{metric} value"
    )
    #fig.show()
    graph_folder = get_graph_folder_path(experiment_descriptor, "model_training")
    graph_title = graph_folder + metric+"_training_history.png"
    fig.write_image(graph_title)


def get_graph_folder_path(experiment_descriptor, kind):
    experiment_folder_path = get_full_experiment_folder(experiment_descriptor)
    image_path = experiment_folder_path + kind + "/" 
    if not os.path.exists(image_path):
        os.mkdir(image_path)
    return image_path

#Reformats the prediction data into something that can be graphed 
def get_usable_pred_data(dataset_descriptor, dataset_result, experiment_result, index=0, kind="full"):
    columns = dataset_descriptor["y_columns"]
    if kind == "full": 
    #Try for one, then you can generalize 
        y_true = dataset_result["y_unnormalized"]
        x_pred = experiment_result["predictions"]["x_pred_unnormalized"]
        y_key = dataset_result["y_key"]
    elif kind == "train":
        y_true = dataset_result["y_train_unnormalized"]
        x_pred = experiment_result["predictions"]["x_pred_train_unnormalized"]
        y_key = dataset_result["y_train_key"]
    elif kind == "test":
        y_true = dataset_result["y_test_unnormalized"]
        x_pred = experiment_result["predictions"]["x_pred_test_unnormalized"]
        y_key = dataset_result["y_test_key"]
    #If we need to reshape
    if y_true.ndim > 2:
        y_true = y_true.reshape(y_true.shape[0]*y_true.shape[1], y_true.shape[2])
    if x_pred.ndim > 2:
        x_pred = x_pred.reshape(x_pred.shape[0]*x_pred.shape[1], x_pred.shape[2])
    if y_key.ndim > 2:
        y_key = y_key.reshape(y_key.shape[0]*y_key.shape[1], y_key.shape[2])
    #Get proper index of values
    y_true = y_true[:, index]
    x_pred = x_pred[:, index]
    y_key = np.squeeze(y_key)
    return y_true, x_pred, y_key


#Graphs the prediction against the actual value
def graph_prediction_against_value(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result, index=0, kind="full"):
    #Works well for 2D ARRAY ONLY. 
    #You need to figure this out for 3D ARRAY Next! 
    columns = dataset_descriptor["y_columns"]
    y_true, x_pred, y_key = get_usable_pred_data(dataset_descriptor, dataset_result, experiment_result, index=index, kind=kind)
    #Create the figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_key, y=y_true, name="True", mode="markers"))
    fig.add_trace(go.Scatter(x=y_key, y=x_pred, name="Predicted", mode="markers"))
    fig.update_layout(
        title=f"{columns[index]} Actual vs Predicted for {kind} set",
        xaxis_title=f"{dataset_descriptor['concat_key']}",
        yaxis_title=f"{columns[index]} value"
    )
    graph_folder = get_graph_folder_path(experiment_descriptor, kind)
    graph_title = graph_folder + str(columns[index])+"_predicted_vs_actual.png"
    fig.write_image(graph_title)
    #fig.show()

#Scatter plot of 
def per_feature_scatter_plot(dataset_descriptor, experiment_descriptor, experiment_result, metric):
    columns = dataset_descriptor["x_columns"]
    #num_columns = len(columns)
    per_feature = experiment_result["per_feature"]
    metric_values = per_feature[metric]
    fig = go.Figure()
    fig.add_trace(go.Bar(x=columns, y=metric_values))
    fig.update_layout(
        title=f"{metric} Values per Feature",
    )
    #fig.show()
    graph_folder = get_graph_folder_path(experiment_descriptor, "per_feature")
    graph_title = graph_folder + str(metric)+"_values_per_feature.png"
    fig.write_image(graph_title)
    

def save_all_per_feature_graphs(dataset_descriptor, experiment_descriptor, experiment_result):
    model_descriptor = experiment_descriptor["model"]
    metrics = model_descriptor["metrics"]
    for metric in metrics: 
        #Should track this down eventually 
        if metric != "loss":
            per_feature_scatter_plot(dataset_descriptor, experiment_descriptor, experiment_result, metric)
        


#Saves graphs on predictions for all features 
def save_all_prediction_graphs(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result): 
    columns = dataset_descriptor["y_columns"]
    num_columns = len(columns)
    kinds = ["full", "train", "test"]
    kinds = ["test"]
    #For each kind
    for dataset_kind in kinds: 
        #For each data variable 
        for i in range(0, num_columns):
            graph_prediction_against_value(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result, index=i, kind=dataset_kind)

def save_all_model_history_graphs(experiment_descriptor, experiment_result):
    model_descriptor = experiment_descriptor["model"]
    metrics = model_descriptor["metrics"]
    for metric in metrics: 
        plot_model_training_history(experiment_descriptor, experiment_result, metric)

def save_to_csv(experiment_descriptor, experiment_result):
    csv_name = "metric_results.csv"
    experiment_folder_path = get_full_experiment_folder(experiment_descriptor)
    save_path = experiment_folder_path+csv_name
    #per_feature = experiment_result["per_feature"]
    test_metrics = experiment_result["test_metrics"].copy()
    test_metrics["training_time"] = experiment_result["training_time"]
    #test_metrics["per_feature"] = test_metrics
    #df = pd.DataFrame.from_dict(test_metrics)
    df = pd.DataFrame.from_dict([test_metrics])
    df.to_csv(save_path)

def save_to_main_csv(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result):
    dict_1 = experiment_result["test_metrics"]
    dict_2 = dataset_descriptor["dataset_class"]
    dict_2.update(dict_1)
    dict_2["dataset_size"] = len(dataset_result["x"])
    dict_2["training_time"] = experiment_result["training_time"]
    dict_2["experiment_name"] = experiment_descriptor["experiment_name"]
    dict_2["dataset_name"] = dataset_descriptor["dataset_name"]
   
    model_descriptor = experiment_descriptor["model"]
    metrics = experiment_result["model_history"]
    num_epochs = len(metrics["loss"])
    dict_2["num_epochs"] = num_epochs
   
    path_name = experiment_descriptor["experiment_folder_path"]+dataset_descriptor["phase_metrics"]+"main_metrics.csv"
    df = pd.DataFrame.from_dict([dict_2])
    #Change header back to false
    df.to_csv(path_name, mode='a', index=False, header=False)


def visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result):
    ##I don't think we need to unnormalize for now. -- but probably want to check your ability
    ##To do so. 
    #unnormalize_data(dataset_descriptor, dataset_result, experiment_result)
    #Later, but not now. 
    #save_all_prediction_graphs(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)
    #save_all_model_history_graphs(experiment_descriptor, experiment_result)
    #save_all_per_feature_graphs(dataset_descriptor, experiment_descriptor, experiment_result)
    save_to_csv(experiment_descriptor, experiment_result)
    save_to_main_csv(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)



def load_everything(experiment_model, dataset_name, path_start=None):
    if path_start:
        path = path_start+"generated_files/experiments/"+experiment_model+"/"+dataset_name+"/"
    else:
        path = "generated_files/experiments/"+experiment_model+"/"+dataset_name+"/"
    names = ["dataset_descriptor", "dataset_result", "experiment_descriptor", "experiment_result"]
    return_dict = {}
    for name in names:
        full_path = path + name + ".pickle"
        with open(full_path, "rb") as f:
                return_dict[name] = pickle.load(f)
    dataset_descriptor = return_dict["dataset_descriptor"]
    dataset_result = return_dict["dataset_result"]
    experiment_descriptor = return_dict["experiment_descriptor"]
    experiment_result = return_dict["experiment_result"]
    return dataset_descriptor, dataset_result, experiment_descriptor, experiment_result


def just_visualize(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result):
    ##I don't think we need to unnormalize for now. -- but probably want to check your ability
    ##To do so. 
    unnormalize_data(dataset_descriptor, dataset_result, experiment_result)
    #Later, but not now. 
    save_all_prediction_graphs(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)
    save_all_model_history_graphs(experiment_descriptor, experiment_result)
    save_all_per_feature_graphs(dataset_descriptor, experiment_descriptor, experiment_result)



#experiment_1 = model_generator.return_test_experiment_descriptor()
#dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.load_in_experiment_files(experiment_1)

#visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)

# print("GRAPH AND VISUALIZE")
# print(dataset_descriptor)
# print(experiment_result)


# history = experiment_result["model_history"]
#     line_list = [history[metric]]
#     text_list = [metric]
#     #fig = px.line(y=history[metric])
#     if val:
#         val_metric = "val_"+metric
#         #fig.add_scatter(y=history[val_metric])
#         line_list.append(history[val_metric])
#         text_list.append(val_metric)
#     fig = px.line(y=line_list, name=text_list)
#     fig.show()


# fig.update_layout(
#     title="Plot Title",
#     xaxis_title="X Axis Title",
#     yaxis_title="Y Axis Title",
#     legend_title="Legend Title",
#     font=dict(
#         family="Courier New, monospace",
#         size=18,
#         color="RebeccaPurple"
#     )
# )