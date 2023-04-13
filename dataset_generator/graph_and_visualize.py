
import pickle
import os
import model_generator
import numpy as np
import plotly.express as px
import plotly.graph_objects as go

#https://plotly.com/python/figure-labels/
#Help for multiple lines: https://www.tutorialspoint.com/how-to-plot-multiple-lines-on-the-same-y-axis-in-python-plotly 
#Numpy indexing: https://stackoverflow.com/questions/42916029/indexing-over-the-last-axis-when-you-dont-know-the-rank-in-advance


def unnormalize_data_transformation(feature_array, dataset_descriptor):
    y_columns = dataset_descriptor["y_columns"]
    reverse_mapping = dataset_descriptor["reverse_mapping"]
    normalization_data = dataset_descriptor["normalization_data"]
    norm_keys = list(normalization_data.keys())
    #For each feature in our feature vector:
    for i in range(0, len(feature_array)):
        name = y_columns[i]
        mapped_item = reverse_mapping[name]
        if mapped_item in list(normalization_data.keys()):
            feature_info = normalization_data[mapped_item]
            max_val = feature_info["max"]
            min_val = feature_info["min"]
            feature_array[i] = (feature_array[i]*(max_val-min_val))+min_val

#Unnormalize data 
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


def plot_model_training_history(experiment_result, metric, val=True):
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
    fig.show()
    
def graph_prediction_against_value(dataset_descriptor, dataset_result, experiment_result, index=0, kind="full"):
    #Works well for 2D ARRAY ONLY. 
    #You need to figure this out for 3D ARRAY Next! 
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
    #Create the figure
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=y_key, y=y_true, name="True", mode="markers"))
    fig.add_trace(go.Scatter(x=y_key, y=x_pred, name="Predicted", mode="markers"))
    fig.update_layout(
        title=f"{columns[index]} Actual vs Predicted for {kind} set",
        xaxis_title=f"{dataset_descriptor['concat_key']}",
        yaxis_title=f"{columns[index]} value"
    )
    fig.show()
    #pass
    
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


def visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result):
    unnormalize_data(dataset_descriptor, dataset_result, experiment_result)
    #plot_model_training_history(experiment_result, "mse", val=True)
    graph_prediction_against_value(dataset_descriptor, dataset_result, experiment_result, index=0, kind="full")



experiment_1 = model_generator.return_test_experiment_descriptor()
dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.load_in_experiment_files(experiment_1)

visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)

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