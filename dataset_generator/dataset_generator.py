import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 

#Reverse_mapping help here: 
#https://www.techiedelight.com/build-dictionary-from-list-of-keys-values-python/

#Pickle help here: https://ianlondon.github.io/blog/pickling-basics/ 
#Help from: https://www.statology.org/pandas-keep-columns/
#From here: https://www.geeksforgeeks.org/how-to-create-an-empty-dataframe-and-append-rows-columns-to-it-in-pandas/
#From here: https://pandas.pydata.org/docs/user_guide/merging.html 
#From here: https://stackoverflow.com/questions/29517072/add-column-to-dataframe-with-constant-value
#https://stackoverflow.com/questions/25254016/get-first-row-value-of-a-given-column 
#https://www.kdnuggets.com/2021/05/deal-with-categorical-data-machine-learning.html 
#https://www.geeksforgeeks.org/how-to-add-and-subtract-days-using-datetime-in-python/
#https://www.geeksforgeeks.org/python-os-makedirs-method/ 
#https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/ 
#https://pbpython.com/categorical-encoding.html 
#https://stackoverflow.com/questions/30510562/get-mapping-of-categorical-variables-in-pandas 
#https://www.geeksforgeeks.org/normalize-a-column-in-pandas/ 
#https://www.w3schools.com/python/python_howto_remove_duplicates.asp 
#https://numpy.org/doc/stable/reference/generated/numpy.load.html 

#Start with JUST One - NPP 
sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
data_streams = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    "wind_300": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min'],
    "wind_150": ['WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min'],
    "wind_75": ['WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
    "wind_dir": ['WinDir_mean_Resultant', 'WinDir_Std_Dev']
}
single_data_streams = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    "wind_300": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min'],
    "wind_150": ['WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min'],
    "wind_75": ['WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
    "wind_dir": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
    "site": ["Sitename"],
    "datetime": ["Date_datetime"]
}

def get_keep_columns(data_streams):
    column_list = []
    for key in list(data_streams.keys()):
        for item in data_streams[key]:
            column_list.append(item)
    return column_list


dataset_1 = {
    "datasets": ["npp_c_cali", "npp_c_grav"],
    "input_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', "Sitename"],
    "output_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min',"Sitename"],
    "categorical": ["Sitename"],
    "normalize": True,
    "input_slices_days": 200,
    "output_slices_days": 1, 
    "output_offset_days": 1,
    "task_type": "regression",
    "clean_method": "drop",
    "concat_key": "Date_datetime",
    "dataset_name": "test_dataset_1",
    "model_index": 0, #0-4? 
    "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
}


# #Note the same column can't be mapped to 2 different names!!! 
# dataset_1 = {
#     "datasets": ["npp_c_cali", "npp_c_grav"],
#     "input_fields": {
#         "npp_c_cali": {
#             "Air_TempC_Avg": "Air_TempC_Avg",
#             "Air_TempC_Max": "Air_TempC_Max"
#         },
#         "npp_c_grav": {
#             "Relative_Humidity_Avg": "Relative_Humidity_Avg",
#             "Relative_Humidity_Max": "Relative_Humidity_Max"
#         },
#     },
#     "output_fields": {
#         "npp_c_cali": {
#             "Air_TempC_Avg": "Air_TempC_Avg",
#             "Air_TempC_Max": "Air_TempC_Max"
#         },
#         "npp_c_grav": {
#             "Relative_Humidity_Avg": "Relative_Humidity_Avg",
#             "Relative_Humidity_Max": "Relative_Humidity_Max",
#         },
#     },
#     "categorical": ["Sitename"],
#     "normalize": True,
#     "input_slices_days": 200,
#     "output_slices_days": 1,
#     "output_offset_days": 1,
#     "task_type": "regression",
#     #"clean_method": "drop",
#     "clean_method": "fill",
#     "concat_key": "Date_datetime",
#     "dataset_name": "test_dataset_1",
#     "model_index": 0, #0-4? 
#     "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
# }


def return_filepath(dataset_object, file_kind):
    model_index = dataset_object["model_index"]
    dataset_name = dataset_object["dataset_name"]
    sub_path = dataset_object["dataset_folder_path"]
    full_path = sub_path+str(model_index)+'/'+dataset_name
    send_path = "" 
    if file_kind == "x":
        send_path = full_path+"_x.npy"
    elif file_kind == "y":
        send_path = full_path+"_y.npy"
    elif file_kind == "x_key":
        send_path = full_path+"_x_key.npy"
    elif file_kind == "y_key":
        send_path = full_path+"_y_key.npy"
    elif file_kind == "dataset_object":
        send_path = full_path+"_dataset_object.json"
    return send_path 

#Returns folder_path,  dataset descriptor filepath and dataset result filepath. 
def get_data_filepaths(dataset_object):
    dataset_name = dataset_object["dataset_name"]
    sub_path = dataset_object["dataset_folder_path"]
    full_path = sub_path+ "/" + str(dataset_name)+"/"
    dataset_result_path = full_path+ "dataset_result.pickle"
    dataset_descriptor_path = full_path+ "dataset_descriptor.pickle"
    return full_path, dataset_result_path, dataset_descriptor_path

def load_in_data(dataset_object):
    full_path, dataset_result_path, dataset_descriptor_path = get_data_filepaths(dataset_object)
    with open(dataset_result_path, "rb") as f:
        dataset_result = pickle.load(f)
    with open(dataset_descriptor_path, "rb") as f:
        dataset_object = pickle.load(f)
    return dataset_result, dataset_object

def save_dataset(x, y, x_key, y_key, dataset_object):
    full_path, dataset_result_path, dataset_descriptor_path = get_data_filepaths(dataset_object)
    os.makedirs(full_path, exist_ok=True)
    #Make the dataset result object. 
    dataset_result = {
        "x": x,
        "y": y,
        "x_key": x_key,
        "y_key": y_key,
    }
    #Save to pickle files.
    with open(dataset_result_path, "wb") as f:
        pickle.dump(dataset_result, f)
    with open(dataset_descriptor_path, "wb") as f:
        pickle.dump(dataset_object, f)


def get_input_output_fields(dataset_object, field_object_index):
    i_fields = dataset_object[field_object_index]
    send_i_fields = []
    if isinstance(i_fields, dict):
        for dataset_name in list(i_fields.keys()):
            prefix = dataset_name + "_"
            fields = list(i_fields[dataset_name].values())
            for item in fields:
                item = prefix + item
                send_i_fields.append(item)
    else:
        dataset_list = dataset_object["datasets"]
        for dataset_name in dataset_list:
            prefix = dataset_name + "_"
            for item in i_fields:
                item = prefix + item
                send_i_fields.append(item)
    return send_i_fields    

#Deal with categorical data 
def handle_categorical(df, dataset_object):
    try:
        categorical_list = dataset_object['categorical']
        if "cat_codes" not in list(dataset_object.keys()):
            dataset_object["cat_codes"] = {}
        for field in categorical_list:
            df[field]= df[field].astype('category')
            field_categories = dict(enumerate(df[field].cat.categories)) 
            #print(field_categories)
            #print(list(df[field].cat.codes))
            df[field] = df[field].cat.codes
            dataset_object["cat_codes"][field] = field_categories
    except Exception as e:
        print("Could not code categorical variables: ", e)
    return df  

#Normalize data 
def normalize_data(df, dataset_object, fields):
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

#Create a dataframe with preprocessed data, and reduce to only necessary data columns 
def create_reduced_dataframe(dataset_name, df, dataset_object):
    normalize = dataset_object["normalize"]
    #Handle categorical variables 
    df = handle_categorical(df, dataset_object)
    #Need input and output fields, concat_key, and renamed here. 
    concat_key = dataset_object["concat_key"]
    i_fields = dataset_object["input_fields"]
    o_fields = dataset_object["output_fields"]
    i_dict = {}
    o_dict = {}
    if isinstance(i_fields, dict):
        i_dict = i_fields[dataset_name]
        i_fields = list(i_fields[dataset_name].keys())
    if isinstance(o_fields, dict):
        o_dict = o_fields[dataset_name]
        o_fields = list(o_fields[dataset_name].keys())
    #Normalize if necessary
    if normalize:
        normalize_fields = i_fields + o_fields
        normalize_fields = list(dict.fromkeys(normalize_fields))
        df = normalize_data(df, dataset_object, normalize_fields)
    keep_cols = i_fields + o_fields + [concat_key]
    df = df[keep_cols]
    if i_dict != {}:
        df = df.rename(columns=i_dict)
    if o_dict != {}:
        df = df.rename(columns=o_dict)
    return df

#Merge the dataframes together, prefixing columns with the dataset they came from 
def create_merged_df(dataset_object):
    whole_df = pd.DataFrame()
    dataset_list = dataset_object["datasets"]
    concat_key = dataset_object["concat_key"]
    input_fields = dataset_object["input_fields"]
    #Will map the renamed field back to its source data, useful for unnormalizing it.  
    reverse_mapping = {}
    #dictionary = dict(zip(keys, values))

    i = 0
    for dataset in dataset_list:
        prefix_string = dataset+"_"
        prefix_concat = prefix_string+concat_key
        #Import the appropriate module 
        module = importlib.import_module(dataset, package=None)
        #Get the dataframe from the module
        df = module.return_data()
        #Reduce where we can 
        df = create_reduced_dataframe(dataset, df, dataset_object)
        #Rename 
        old_columns = list(df.columns)
        df = df.add_prefix(prefix_string)
        df = df.rename(columns={prefix_concat: concat_key})
        new_columns = list(df.columns)
        mapping = dict(zip(new_columns, old_columns))
        reverse_mapping.update(mapping)
        #Merge 
        if i > 0:
            #whole_df = pd.merge(whole_df, df, on=concat_key)
            whole_df = pd.merge(df, whole_df, on=concat_key)
        else:
            whole_df = df
        i = i+1
    dataset_object["reverse_mapping"] = reverse_mapping
    #Change is here
    return whole_df 

#Drop or fill missing data (recommend fill)
def deal_with_missing_data(df, dataset_object):
    clean_method = dataset_object["clean_method"]
    if clean_method == "drop": 
        df = df.dropna()
        #Line gets rid of dropped data 
        df = df.reset_index(drop=True)
    elif clean_method == "fill":
        df = df.fillna(method="pad")
    return df

#Take a slice and make it a numpy array 
def slice_to_numpy(df, x_start, y_start, x_end, y_end, x_cols, y_cols, input_fields, output_fields):
    #Get the proper slice 
    x = df.loc[x_start:x_end, :]
    y = df.loc[y_start:y_end, :]
    #Restrict to only the input and output fields we are using 
    x = x[input_fields]
    y = y[output_fields]
    #Change from a dataframe to the vector we want 
    x_array = x.to_numpy()
    y_array = y.to_numpy()
    return x_array, y_array

#Time Slice! 
#This also assumes you already have the data columns you want. 
#This time slice function assumes there are no day gaps - I think this works for 
#this dataset, but is probably not broadly applicable 
def time_slice(dataset_object, df):
    input_slices_days = dataset_object["input_slices_days"]
    output_slices_days = dataset_object["output_slices_days"]
    output_offset_days = dataset_object["output_offset_days"]
    input_fields = get_input_output_fields(dataset_object, "input_fields")
    output_fields = get_input_output_fields(dataset_object, "output_fields")
    concat_key_fields = [dataset_object["concat_key"]]
    x_cols = df[input_fields]
    y_cols = df[output_fields]
    dataset_object["x_columns"] = list(x_cols.columns)
    dataset_object["y_columns"] = list(y_cols.columns)
    print("Dataset object ", dataset_object)
    num_rows = len(df)
    x_vect = []
    y_vect = []
    x_key = []
    y_key = []
    x_start = 0
    x_end = input_slices_days-1
    y_start = x_end+output_offset_days
    y_end = y_start+output_slices_days-1
    #Get x and y values indexed properly. 
    while y_end < num_rows-1:
        x_array, y_array = slice_to_numpy(df, x_start, y_start, x_end, y_end, x_cols, y_cols, input_fields, output_fields)
        x_key_array, y_key_array = slice_to_numpy(df, x_start, y_start, x_end, y_end, x_cols, y_cols, concat_key_fields, concat_key_fields)
        if output_slices_days <= 1:
            y_array = y_array[0]
            y_key_array = y_key_array[0]
        #Add to our samples
        x_vect.append(x_array)
        y_vect.append(y_array)
        x_key.append(x_key_array)
        y_key.append(y_key_array)
        #Increment
        x_start = x_start+1
        x_end = x_end+1
        y_start = y_start+1
        y_end = y_end+1
    #Finally, convert to a numpy array 
    x_vect = np.array(x_vect)
    y_vect = np.array(y_vect)
    x_key = np.array(x_key)
    y_key = np.array(y_key)
    print("Number of x samples", len(x_vect))
    print("Number of y samples", len(y_vect))
    print("First x sample", x_vect[0])
    print("First y sample", y_vect[0])
    # print("First x key", x_key[0])
    # print("First y key", y_key[0])
    print("X shape:", x_vect.shape)
    print("Y shape:", y_vect.shape)
    return x_vect, y_vect, x_key, y_key


#Take in a dataset object, create it, and save it. 
#Takes in a dataset object, returns 
def create_dataset_from_dataset_object(dataset_object):
    #1. Creates the merged dataset with the necessary fields 
    df = create_merged_df(dataset_object)
    #2. Drop or fill N/A data 
    df = deal_with_missing_data(df, dataset_object)
    print(df.describe())
    print(list(df.columns))
    print("--------------")
    #3. Time Slice 
    x_vect, y_vect, x_key, y_key = time_slice(dataset_object, df)
    #4. Save. 
    save_dataset(x_vect, y_vect, x_key, y_key, dataset_object)
    return x_vect, y_vect, x_key, y_key, dataset_object


#create_dataset_from_dataset_object(dataset_1)

#dataset_result, dataset_descriptor = load_in_data(dataset_1)
#print(dataset_result, dataset_descriptor)


def return_test_dataset():
    dataset_result, dataset_descriptor = load_in_data(dataset_1)
    return dataset_result, dataset_descriptor



#NOTES - You need to better define your saving/loading naming schema for a particular dataset. 

# EXPERIMENT
# Layers: (dict)
#     key with num layer index, 
#     nodes: number of nodes (value)
#     activation_function: activation function
# Optimization (Like adam)
# Initial LR
# Number of epochs?
# Early stopping
# Metrics (list)
# Model save path (do you need multiple? Maybe per number of epochs)
# Save values (model history) - what to save 
# Save path as well ...

#Tomorrow - start with figuring out your scaling
#Maybe small network just to check 
#Also loading in the dataset. 









# def save_dataset(x, y, x_key, y_key, dataset_object):
#     dataset_name = dataset_object["dataset_name"]
#     sub_path = dataset_object["dataset_folder_path"]
#     full_path = sub_path+ "/" + str(dataset_name)
#     os.makedirs(full_path, exist_ok=True)

#     dataset_result_path = full_path+ "_dataset_result.pickle"
#     dataset_descriptor_path = full_path+ "_dataset_descriptor.pickle"
#     # x_path = full_path+"/"+dataset_name+"_x.npy"
#     # y_path = full_path+"/"+dataset_name+"_y.npy"
#     # x_key_path = full_path+"/"+dataset_name+"_x_key.npy"
#     # y_key_path = full_path+"/"+dataset_name+"_y_key.npy"
#     # d_obj_path = full_path+"/"+dataset_name+"_dataset_object.json"

#     np.save(x_path, x)
#     np.save(y_path, y)
#     np.save(x_key_path, x_key)
#     np.save(y_key_path, y_key)
#     dataset_descriptor = json.dumps(dataset_object)
#     with open(d_obj_path, "w") as f:
#         f.write(dataset_descriptor)




# def load_in_file(dataset_object, file_kind):
#     filepath = return_filepath(dataset_object, file_kind)
#     if file_kind == "x" or file_kind == "y" or file_kind == "x_key" or file_kind == "y_key": 
#         loaded_file = np.load(filepath)
#         return loaded_file
#     elif file_kind == "dataset_object":
#         f = open(filepath)
#         loaded_file = json.load(f)
#         f.close()
#         return loaded_file
#     return {}
