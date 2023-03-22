import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 

#Help from: https://www.statology.org/pandas-keep-columns/
#From here: https://www.geeksforgeeks.org/how-to-create-an-empty-dataframe-and-append-rows-columns-to-it-in-pandas/
#From here: https://pandas.pydata.org/docs/user_guide/merging.html 
#From here: https://stackoverflow.com/questions/29517072/add-column-to-dataframe-with-constant-value
#https://stackoverflow.com/questions/25254016/get-first-row-value-of-a-given-column 
#https://www.kdnuggets.com/2021/05/deal-with-categorical-data-machine-learning.html 
#https://www.geeksforgeeks.org/how-to-add-and-subtract-days-using-datetime-in-python/
#https://www.geeksforgeeks.org/python-os-makedirs-method/ 
#https://machinelearningmastery.com/how-to-save-a-numpy-array-to-file-for-machine-learning/ 

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
    "input_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "output_dataset": ["npp_c_cali"],
    "output_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
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


# # #Note the same column can't be mapped to 2 different names!!! 
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
#     "output_dataset": ["npp_c_cali"],
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


def save_dataset(x, y, dataset_object):
    model_index = dataset_object["model_index"]
    dataset_name = dataset_object["dataset_name"]
    sub_path = dataset_object["dataset_folder_path"]
    full_path = sub_path+str(model_index)
    os.makedirs(full_path, exist_ok=True)
    x_path = full_path+"/"+dataset_name+"_x.npy"
    y_path = full_path+"/"+dataset_name+"_y.npy"
    d_obj_path = full_path+"/"+dataset_name+"_descriptor.json"
    print(x_path, y_path, d_obj_path)
    np.save(x_path, x)
    np.save(y_path, y)
    dataset_descriptor = json.dumps(dataset_object)
    with open(d_obj_path, "w") as f:
        f.write(dataset_descriptor)
     

    # os.makedirs('folder/subfolder', exist_ok=True)  
    # df.to_csv('folder/subfolder/out.csv')  


# with open("sample.json", "w") as outfile:
#     outfile.write(json_object)

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


def create_reduced_dataframe(dataset_name, df, dataset_object):
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
    keep_cols = i_fields + o_fields + [concat_key]
    df = df[keep_cols]
    if i_dict != {}:
        df = df.rename(columns=i_dict)
    if o_dict != {}:
        df = df.rename(columns=o_dict)
    return df

def create_merged_df(dataset_object):
    whole_df = pd.DataFrame()
    dataset_list = dataset_object["datasets"]
    concat_key = dataset_object["concat_key"]
    input_fields = dataset_object["input_fields"]
    i = 0
    for dataset in dataset_list:
        prefix_string = dataset+"_"
        prefix_concat = prefix_string+concat_key
        #Import the appropriate module 
        module = importlib.import_module(dataset, package=None)
        #Get the dataframe from the module
        df = module.return_data()
        #Reduce and Rename where necessary
        df = create_reduced_dataframe(dataset, df, dataset_object)
        df = df.add_prefix(prefix_string)
        df = df.rename(columns={prefix_concat: concat_key})
        if i > 0:
            #whole_df = pd.merge(whole_df, df, on=concat_key)
            whole_df = pd.merge(df, whole_df, on=concat_key)
        else:
            whole_df = df
        i = i+1
    return whole_df 

def deal_with_missing_data(df, dataset_object):
    clean_method = dataset_object["clean_method"]
    if clean_method == "drop": 
        df = df.dropna()
        #Line gets rid of dropped data 
        df = df.reset_index(drop=True)
    elif clean_method == "fill":
        df = df.fillna(method="pad")
    return df

#NEEDS MORE WORK - Need to restrict the outputs I think 
#This also assumes you already have the data columns you want. 
#This time slice function assumes there are no day gaps - I think this works for 
#this dataset, but is probably not broadly applicable 
def time_slice(dataset_object, df):
    input_slices_days = dataset_object["input_slices_days"]
    output_slices_days = dataset_object["output_slices_days"]
    output_offset_days = dataset_object["output_offset_days"]
    input_fields = get_input_output_fields(dataset_object, "input_fields")
    output_fields = get_input_output_fields(dataset_object, "output_fields")
    num_rows = len(df)
    x_vect = []
    y_vect = []
    x_start = 0
    x_end = input_slices_days-1
    y_start = x_end+output_offset_days
    y_end = y_start+output_slices_days-1
    #Get x and y values indexed properly. 
    while y_end < num_rows-1:
        #Get the proper slice 
        x = df.loc[x_start:x_end, :]
        y = df.loc[y_start:y_end, :]
        #Restrict to only the input and output fields we are using 
        x = x[input_fields]
        y = y[output_fields]
        #Change from a dataframe to the vector we want 
        x_array = x.to_numpy()
        y_array = y.to_numpy()
        if output_slices_days <= 1:
            y_array = y_array[0]
        #Add to our samples
        x_vect.append(x_array)
        y_vect.append(y_array)
        #Increment
        x_start = x_start+1
        x_end = x_end+1
        y_start = y_start+1
        y_end = y_end+1
    #Finally, convert to a numpy array 
    x_vect = np.array(x_vect)
    y_vect = np.array(y_vect)

    print("Number of x samples", len(x_vect))
    print("Number of y samples", len(y_vect))
    print("First x sample", x_vect[0])
    print("First y sample", y_vect[0])
    print("X shape:", x_vect.shape)
    print("Y shape:", y_vect.shape)
    return x_vect, y_vect 




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
    x_vect, y_vect = time_slice(dataset_object, df)
    #4. Save. 
    #save_dataset(x_vect, y_vect, dataset_object)


create_dataset_from_dataset_object(dataset_1)

#NOTES - You need to better define your saving/loading naming schema for a particular dataset. 
#You need to save the column name order (and maybe the timestamp???) when you save the dataset. 
#Maybe add to the dataset object?  -START HERE NEXT! 
#Would be nice to get from the dataset object. 

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


