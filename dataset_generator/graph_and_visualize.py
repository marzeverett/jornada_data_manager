
import pickle
import os
import model_generator

#Numpy indexing: https://stackoverflow.com/questions/42916029/indexing-over-the-last-axis-when-you-dont-know-the-rank-in-advance


#Normalize data - Figure this out later. 
def unnormalize_data(dataset_descriptor, dataset_result):
    y_map = {
        "y": "y_unnormalize",
        "y_train": "y_train_unnormalize",
        "y_test": "y_test_unnormalize"
    }

    y_columns = dataset_descriptor["y_columns"]
    print(y_columns)
    normalization_data = dataset_descriptor["normalization_data"]

    #b = a[..., -k:]
    for y_key in list(y_map.keys()): 
        y_vals = dataset_result[y_key].copy()
        print(y_vals.shape)
        #Get second to last index (where samples lives)
        #y_samples = y_vals[..., -2:]
        print(len(y_columns))
        print(y_samples.shape)
        for i in range(0, len(y_vals)):
            #This gets us down to an individual feature vector.
            feature_vector = y_samples[i]
            column_name = y_columns[i]
            #print(feature_vector)
            #print(y_columns)


    #y columns will either be 2D or 3D. 


    concat_key = dataset_object["concat_key"]
    if "normalization_data" not in list(dataset_object.keys()):
        dataset_object["normalization_data"] = {}
    #From the geeks for geeks tutorial on normalization 
    for field in fields: 
        if field != "concat_key":
            max_val = df[field].max()
            min_val = df[field].min()
            n_dict = {
                "max": max_val,
                "min": min_val
            }
            diff_between = max_val - min_val
            #Handle potential divide by zero issue 
            if diff_between != 0:
                df[field] = (df[field] - min_val) / (max_val - min_val)
                dataset_object["normalization_data"][field] = n_dict
    return df 



def visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result):
    unnormalize_data(dataset_descriptor, dataset_result)


experiment_1 = model_generator.return_test_experiment_descriptor()
dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.load_in_experiment_files(experiment_1)

visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)

# print("GRAPH AND VISUALIZE")
# print(dataset_descriptor)
# print(experiment_result)