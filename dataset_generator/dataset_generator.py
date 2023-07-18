import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 
os.environ['TF_CPP_MIN_LOG_LEVEL']  = '3'
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
from tensorflow.keras import datasets, layers, models

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
#https://sparkbyexamples.com/pandas/pandas-drop-columns-with-nan-none-values/  
#https://www.techbeamers.com/program-python-list-contains-elements/ 
#https://stackoverflow.com/questions/42916029/indexing-over-the-last-axis-when-you-dont-know-the-rank-in-advance 






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

def save_dataset(x, y, x_key, y_key, x_raw, y_raw, dataset_object):
    full_path, dataset_result_path, dataset_descriptor_path = get_data_filepaths(dataset_object)
    os.makedirs(full_path, exist_ok=True)
    #Make the dataset result object. 
    dataset_result = {
        "x": x,
        "y": y,
        "x_key": x_key,
        "y_key": y_key,
        "x_raw": x_raw,
        "y_raw": y_raw
    }
    #Save to pickle files.
    with open(dataset_result_path, "wb") as f:
        pickle.dump(dataset_result, f, protocol=4)
    with open(dataset_descriptor_path, "wb") as f:
        pickle.dump(dataset_object, f, protocol=4)


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
def normalize_data(dataset_name, df, dataset_object, fields):
    prefix_string = dataset_name+"_"
    concat_key = dataset_object["concat_key"]
    if "normalization_data" not in list(dataset_object.keys()):
        dataset_object["normalization_data"] = {}
    #From the geeks for geeks tutorial on normalization 
    for field in fields: 
        if field != "concat_key":
            try:
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
                    field_name = prefix_string+field
                    dataset_object["normalization_data"][field_name] = n_dict
            except Exception as e:
                pass
    return df 

#Create a dataframe with preprocessed data, and reduce to only necessary data columns 
def create_reduced_dataframe(dataset_name, df, dataset_object):
    normalize = dataset_object["normalize"]
    #Handle categorical variables 
    df = handle_categorical(df, dataset_object)

    #If prediction task, handle here 
    if "predict_type" in list(dataset_object.keys()):
        predict_type = dataset_object["predict_type"]
        if predict_type == "frost":
            df['frost'] = np.where(df['Air_TempC_Min'] < 0, 1, 0)
        if predict_type == "storm":
            df['storm'] = np.where(df['Ppt_mm_Tot'] >= 10, 1, 0)
    #Need input and output fields, concat_key, and renamed here. 
    concat_key = dataset_object["concat_key"]
    i_fields = dataset_object["input_fields"]
    o_fields = dataset_object["output_fields"]
    i_dict = {}
    o_dict = {}
    if isinstance(i_fields, dict):
        if dataset_name in list(i_fields.keys()):
            i_dict = i_fields[dataset_name]
            i_fields = list(i_fields[dataset_name].keys())
        else:
            i_fields = []
    if isinstance(o_fields, dict):
        if dataset_name in list(o_fields.keys()):
            o_dict = o_fields[dataset_name]
            o_fields = list(o_fields[dataset_name].keys())
        else:
            o_fields = []
    #Normalize if necessary
    if normalize:
        normalize_fields = i_fields + o_fields
        normalize_fields = list(dict.fromkeys(normalize_fields))
        df = normalize_data(dataset_name, df, dataset_object, normalize_fields)
    keep_cols = i_fields + o_fields + [concat_key]

    #Handle any missing cols 
    actual_cols = list(df.columns)
    final_cols = list(set(keep_cols) & set(actual_cols))
    df = df[final_cols]
    #df = df[keep_cols]

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
        save_name = "pickled_datasets/"+dataset+".pkl"
        df = pd.read_pickle(save_name)
        #Drop any columns that are all NaN
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
        #Drop columns that you can't pad. 
        #This shifts data that was missing to the time period it was available. 
        #Since we filled ahead of time. 
        df= df.dropna()
        df = df.reset_index(drop=True)
    return df

#Don't have great error checking on this... 
#But it gets the latent space. Admittedly, this could fail with latent space being []
#But in that case it probably should fail... 
def get_ae_latent_space(path, x_columns, x_vect, x_key_vect):
    full_model_path = path + "latent_model"
    ae_model = models.load_model(full_model_path)
    full_dd_path = path+"dataset_descriptor.pickle"
    latent_space = [] 
    with open(full_dd_path, "rb") as f:
        dataset_object = pickle.load(f)
    #Recursive case - this depends on other AEs
    if "ae_paths" in list(dataset_object.keys()):
        ae_paths = dataset_object["ae_paths"]
        for path in ae_paths:
            ae_output = get_ae_latent_space(path, x_columns, x_vect,x_key_vect)
            if latent_space == []:
                 latent_space = ae_output
            else:
                 #This should actually work, but should definitely check. 
                 latent_space = np.hstack((latent_space, ae_output))
    #Base case - model does not depend on AE outputs 
    else:
        model_inputs = dataset_object["x_columns"]
        relevant_indexes = []
        #This is the part we'll have to change if conv. 
        for input_col in model_inputs:
            relevant_indexes.append(x_columns.index(input_col))
        ae_input = x_vect[:, relevant_indexes]
        # print("Here")
        # print(ae_input.shape)
        # print(ae_model.summary())
        latent_space = ae_model.predict(ae_input)
    return latent_space

 #This function could use a LOT better documentation    
def process_aes(dataset_object, x_vect, x_key_vect):
    ae_paths = dataset_object["ae_paths"]
    #execute_list, ae_dict = build_ae_tree(ae_paths)
    x_columns = dataset_object["x_columns"]
    #For each identified autoencoder, in each stage. 
    #CHECK
    latent_space = []
    #latent_space = []
    for path in ae_paths:
        ae_output = get_ae_latent_space(path, x_columns, x_vect, x_key_vect)
        if latent_space == []:
            latent_space = ae_output
        else:
            latent_space = np.hstack((latent_space, ae_output))

    return latent_space, x_key_vect


#This makes sure only columns present both in the spec and the dataset make it in. 
def get_actual_input_output_columns(dataset_object, df):
    input_fields = get_input_output_fields(dataset_object, "input_fields")
    output_fields = get_input_output_fields(dataset_object, "output_fields")
    actual_cols = list(df.columns)
    actual_input = list(set(input_fields)&set(actual_cols))
    actual_output = list(set(output_fields)&set(actual_cols))
    return actual_input, actual_output

#Time Slice! 
#This also assumes you already have the data columns you want. 
#This time slice function assumes there are no day gaps - I think this works for 
#this dataset, but is probably not broadly applicable 
def time_slice(df, dataset_object, x, y, x_key, y_key):
    input_slices_days = dataset_object["input_slices_days"]
    output_slices_days = dataset_object["output_slices_days"]
    output_offset_days = dataset_object["output_offset_days"]
    num_rows = len(df)
    x_vect, y_vect, x_key_vect, y_key_vect = [], [], [], []
    x_start = 0
    x_end = input_slices_days-1
    y_start = x_end+output_offset_days
    y_end = y_start+output_slices_days-1
    #Get x and y values indexed properly. 
    while y_end < num_rows-1:
        x_array = x[x_start:x_end+1]
        x_key_array = x_key[x_start:x_end+1]
        if y_start == y_end:
            y_array = y[y_start]
            y_key_array = y_key[y_start]
        else:
            y_array = y[y_start:y_end+1]
            y_key_array = y_key[y_start:y_end+1]
        x_vect.append(x_array)
        y_vect.append(y_array)
        x_key_vect.append(x_key_array)
        y_key_vect.append(y_key_array)
        #If it is nested, this is where we go for it. 
        #Increment    
        x_start = x_start+1
        x_end = x_end+1
        y_start = y_start+1
        y_end = y_end+1
    #Finally, convert to a numpy array 
    x_vect = np.array(x_vect)
    y_vect = np.array(y_vect)
    x_key_vect = np.array(x_key_vect)
    y_key_vect = np.array(y_key_vect)
    return x_vect, y_vect, x_key_vect, y_key_vect

# #Going to have to think about more -- basically need this 
# #On a per-site basis... 
# def analyze_y_array(predict_type, y_raw_array):
#     if predict_type == "frost":
#         if 
# def time_slice_predict(df, dataset_object, x, y, x_key, y_key, x_raw, y_raw, predict_type="frost", y_cols):
#     input_slices_days = dataset_object["input_slices_days"]
#     output_slices_days = dataset_object["output_slices_days"]
#     output_offset_days = dataset_object["output_offset_days"]
#     num_rows = len(df)
#     x_vect, y_vect, x_key_vect, y_key_vect = [], [], [], []
#     x_start = 0
#     x_end = input_slices_days-1
#     y_start = x_end+output_offset_days
#     y_end = y_start+output_slices_days-1
#     #Get x and y values indexed properly. 
#     while y_end < num_rows-1:
#         x_array = x[x_start:x_end+1]
#         x_key_array = x_key[x_start:x_end+1]
#         if y_start == y_end:
#             y_array = y[y_start]
#             y_key_array = y_key[y_start]
#             y_raw_array = y_raw[y_start]
#         else:
#             y_array = y[y_start:y_end+1]
#             y_key_array = y_key[y_start:y_end+1]
#             y_raw_array = y_raw[y_start:y_end+1]
#         #Add the slices 
#         x_vect.append(x_array)
#         #Here's where we change things up a bit. 
#         y_array = analyze_y_array(predict_type, y_raw_array)
#         y_vect.append(y_array)
#         x_key_vect.append(x_key_array)
#         y_key_vect.append(y_key_array)
#         #If it is nested, this is where we go for it. 
#         #Increment    
#         x_start = x_start+1
#         x_end = x_end+1
#         y_start = y_start+1
#         y_end = y_end+1
#     #Finally, convert to a numpy array 
#     x_vect = np.array(x_vect)
#     y_vect = np.array(y_vect)
#     x_key_vect = np.array(x_key_vect)
#     y_key_vect = np.array(y_key_vect)
#     return x_vect, y_vect, x_key_vect, y_key_vect

#Prints stuff. Kinda useful for debugging. 
def print_output_data_info(actual_input, x_vect, y_vect, x_key, y_key):
    print("Cols ", actual_input)
    print("Number of x samples", len(x_vect))
    print("Number of y samples", len(y_vect))
    print("First x sample", x_vect[0])
    print("First y sample", y_vect[0])
    print("x_key_shape", x_key.shape)
    print("y_key shape", y_key.shape)
    #print("First x key", x_key[0])
    #print("First y key", y_key[0])
    print("X shape:", x_vect.shape)
    print("Y shape:", y_vect.shape)

#Formats the data so the model can accept it
#Takes care of autoencoders preprocessing and time-slicing, too. 
def format_data_model_ready(dataset_object, df):
    target_model = dataset_object["target_model"]
    concat_key_fields = [dataset_object["concat_key"]]
    #Handles any missing columns 
    actual_input, actual_output = get_actual_input_output_columns(dataset_object, df)
    #Slice x and y, and x and y keys. Add this info to the dataset descriptor
    x_cols = df[actual_input]
    y_cols = df[actual_output]
    key_cols = df[concat_key_fields]
    x_cols_names = list(x_cols.columns)
    y_cols_names = list(y_cols.columns)
    dataset_object["x_columns"] = x_cols_names
    dataset_object["y_columns"] = y_cols_names
    #Convert to numpy array
    x_vect = x_cols.to_numpy()
    y_vect = y_cols.to_numpy()
    x_key_vect = key_cols.to_numpy()
    y_key_vect = key_cols.to_numpy()

    x_raw = x_vect
    y_raw = y_vect

    if dataset_object["conv"] == True and dataset_object["conv_and_prev_ae"] == False:
        x_matrix, y_matrix = matricize_dataset(x_vect, y_vect, dataset_object)
        x_vect = x_matrix
        y_vect = y_matrix
    #If this model needs to be preprocessed through an ae, do that first
    if "ae_paths" in list(dataset_object.keys()):
        x_vect, x_key_vect = process_aes(dataset_object, x_vect, x_key_vect)
    #If this is a time regression model, we need to slice it up. 
    if target_model == "time_regression" or target_model == "time_predict":
        #For conv? - Maybe CHECK, CHANGE HERE 
        y_vect = y_raw
        x_vect, y_vect, x_key_vect, y_key_vect = time_slice(df, dataset_object, x_vect, y_vect, x_key_vect, y_key_vect)
    #Change also here 
    #print_output_data_info(actual_input, x_vect, y_vect, x_key_vect, y_key_vect)
    return x_vect, y_vect, x_key_vect, y_key_vect, x_raw, y_raw


def print_dataset_info(df):
    print(df.describe())
    print(list(df.columns))
    print("--------------")

def feature_map_to_feature_vect(x_vect, grid, matrix_map, x_columns, channels):
    for i in range(0, len(x_columns)):
        if x_columns[i] in list(matrix_map.keys()):
            indexes = matrix_map[x_columns[i]]
            grid[i] = x_vect[indexes[0], indexes[1], indexes[2]] 
    return grid

def feature_vect_to_feature_map(x_vect, grid, matrix_map, x_columns, channels):
    for i in range(0, len(x_columns)):
        if x_columns[i] in list(matrix_map.keys()):
            indexes = matrix_map[x_columns[i]]
            grid[indexes[0], indexes[1], indexes[2]] = x_vect[i]
    return grid
        
def matrix_map(x_columns, channels, coords, sites, dataset_object):
    #need 3D index
    #x, y, channel 
    matrix_map = {}
    for column in x_columns:
        info = column.split("_")
        #A bit ugly, but it works - dependent on the format we have the data in, currently 
        site = "_".join(info[0:3])
        datastream = "_".join(info[3:])
        try:
            channel_index = channels.index(datastream)
            site_index = sites.index(site)
            full_index = [coords[site_index][0], coords[site_index][1], channel_index]
            matrix_map[column] = full_index
        except Exception as e:
            pass
    return matrix_map
        
    
#Get information channels present in dataset 
def get_channels(x_columns, image_map, dataset_object):
    #Get all channels 
    feature_indexes = []
    site_indexes = []
    site_names = image_map["sites"]
    raw_channels = x_columns.copy()
    channels = []
    #Take out all relevant site names
    for item in raw_channels:
        for site in site_names:
            if site in item:
                replace_string = site+"_"
                channels.append(item.replace(replace_string, ''))
    channels = list(set(channels))
    return channels 
    

# #This is not working. It may be ok to not implement?? 
# def unmatricize_dataset(x_vect, y_vect, dataset_object):
#     x_columns = dataset_object['x_columns']
#     channels = dataset_object["channels"]
#     matrix = dataset_object["matrix_map"]
#     grid = []
#     dimension = x_vect.ndim
#     iter_dim = dimension - 3
#     new_vect = x_vect[:iter_dim]
#     other_vect = x_vect[iter_dim:]
#     yes_vect = x_vect[..., iter_dim:]
#     no_vect = x_vect[...,:iter_dim]
#     final_vect = x_vect[:, :, ...]
#     print("AQUI")
#     print(new_vect.shape)
#     print(other_vect.shape)
#     print(yes_vect.shape)
#     print(no_vect.shape)
#     print(final_vect.shape)
#     for arr in np.nditer(x_vect, op_axes=[[-3, -2, -1]]):
#         print("X vector slice?")
#         print(arr.shape)
#         arr = feature_map_to_feature_vect(arr, grid.copy(), matrix, x_columns, channels) 
#     print(x_vect.shape)

def matricize_dataset(x_vect, y_vect, dataset_object):
    x_columns = dataset_object['x_columns']
    y_columns = dataset_object['y_columns'] 
    #Loads in the dictionary 
    with open("image_map.pkl", "rb") as f:
        image_map = pickle.load(f)
    #Get the channels used 
    x_channels = get_channels(x_columns, image_map, dataset_object)
    y_channels = get_channels(y_columns, image_map, dataset_object)
    dataset_object["x_channels"] = x_channels
    dataset_object["y_channels"] = y_channels
    #Get the image map information 
    coords = image_map["coords"]
    site_names = image_map["sites"]
    grid_size = image_map["grid_size"]

    x_matrix_map = matrix_map(x_columns, x_channels, coords, site_names, dataset_object)
    y_matrix_map = matrix_map(y_columns, y_channels, coords, site_names, dataset_object)
    dataset_object["x_matrix_map"] = x_matrix_map
    dataset_object["y_matrix_map"] = y_matrix_map
    print("Before")
    print(x_vect.shape)
    x_grid = np.zeros((grid_size, grid_size, len(x_channels)))
    y_grid = np.zeros((grid_size, grid_size, len(y_channels)))
    x_matrix = np.apply_along_axis(feature_vect_to_feature_map, -1, x_vect, np.copy(x_grid), x_matrix_map, x_columns, x_channels)
    y_matrix = np.apply_along_axis(feature_vect_to_feature_map, -1, y_vect, np.copy(y_grid), y_matrix_map, y_columns, y_channels)

    print("After - Vect then returned matrix")
    print(x_vect.shape)
    print(x_matrix.shape)
    print(y_vect.shape)
    print(y_matrix.shape)
    return x_matrix, y_matrix 

#Take in a dataset object, create it, and save it. 
#Takes in a dataset object, returns 
def create_dataset_from_dataset_object(dataset_object):
    #1. Creates the merged dataset with the necessary fields 
    df = create_merged_df(dataset_object)
    #2. Drop or fill N/A data
    df = deal_with_missing_data(df, dataset_object)
    #Change here
    #print_dataset_info(df)
    #3. Format for Keras model - this handles LSTM, AE, and (soon) Nested
    x_vect, y_vect, x_key, y_key, x_raw, y_raw = format_data_model_ready(dataset_object, df)                  
    #4. Save. 
    save_dataset(x_vect, y_vect, x_key, y_key, x_raw, y_raw, dataset_object)
    return x_vect, y_vect, x_key, y_key, dataset_object


def return_test_dataset():
    dataset_result, dataset_descriptor = load_in_data(dataset_1)
    return dataset_result, dataset_descriptor


# dataset_1 = {
#     "target_model": "time_regression",
#     "datasets": ["npp_c_cali", "npp_c_grav"],
#     "input_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', "Sitename"],
#     "output_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min',"Sitename"],
#     "categorical": ["Sitename"],
#     "normalize": True,
#     "input_slices_days": 200,
#     "output_slices_days": 1, 
#     "output_offset_days": 1,
#     "task_type": "regression",
#     "clean_method": "drop",
#     "concat_key": "Date_datetime",
#     "dataset_name": "test_dataset_1",
#     "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
# }


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
#     "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
# }


