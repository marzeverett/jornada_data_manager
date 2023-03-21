import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta

#Help from: https://www.statology.org/pandas-keep-columns/
#From here: https://www.geeksforgeeks.org/how-to-create-an-empty-dataframe-and-append-rows-columns-to-it-in-pandas/
#From here: https://pandas.pydata.org/docs/user_guide/merging.html 
#From here: https://stackoverflow.com/questions/29517072/add-column-to-dataframe-with-constant-value
#https://stackoverflow.com/questions/25254016/get-first-row-value-of-a-given-column 
#https://www.kdnuggets.com/2021/05/deal-with-categorical-data-machine-learning.html 
#https://www.geeksforgeeks.org/how-to-add-and-subtract-days-using-datetime-in-python/

#Start with JUST One - NPP 
sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
mapping_dict = {

}

data_streams = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    "wind_300": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min'],
    "wind_150": ['WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min'],
    "wind_75": ['WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
    "wind_dir": ['WinDir_mean_Resultant', 'WinDir_Std_Dev']
}

prediction_tasks = {

}


coordinates = {
}

def one_big_dataset():
    #sites = ["c_cali"]
    new_df = pd.DataFrame()
    for site in sites:
        import_string = "npp_"+site
        module = importlib.import_module(import_string, package=None)
        temp_df = module.return_data()
        #Add site column
        temp_df["site"] = site
        #Only keep certain columns
        #temp_df = temp_df[['Air_TempC_Avg', 'Air_TempC_Max']]
        new_df = pd.concat([new_df,temp_df])
    
    print(new_df.describe())
    print(list(new_df.columns))

#one_big_dataset()

#Sort by datetime (day), etc. 

#Add column 
#df["site"] = site_code

#Concat our dataframes: 
#pd.concat([list, of, dataframes])

#Date_datetime

def generate_dataset():
    import npp_t_west
    dt = npp_t_west.return_data()
    print(dt.describe())

#generate_dataset()
#Takes in: 
#   inputs: key-value pairs 
#       dataset: (name of dataset(s))
#       fields: (which_fields)
#       instances: (which_instances)
#   by_instance (T/F) (Add Code identifying instance)
#   rid_empty (T/F) get rid of empty dataset fields
#   encode (T/F)
#   

def time_slices():
    pass
#Psuedo-code


#Takes in:
 #  dataset: 
 #  time_slices
 #  output_time_slices:


def generate_spatial_dataset():
    pass

#For each - if number not correct, throw it out. 

#Start with one dataset, completely ready for LSTM use. 
#"Sitename"
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



#Number of samples in one sequence 
time_steps = 200
#Want to predict starting one day ahead 
days_ahead = 1
#Only want to predict one day
num_days_ahead = 0

#This does NOT deal gracefully so far with our missing values! 
#This also assumes you already have the data columns you want. 
def time_slice_naive(df, time_steps, days_ahead, num_days_ahead): 
    num_rows = len(df)
    x_vect = []
    y_vect = []
    x_start = 0
    x_end = time_steps-1
    y_start = time_steps+days_ahead
    y_end = y_start+num_days_ahead
    #Get x and y values indexed properly. 
    while y_end < num_rows-1:
        #Get the proper slice 
        x = df.loc[x_start:x_end, :]
        y = df.loc[y_start:y_end, :]
        #Change from a dataframe to the vector we want 
        x_array = x.to_numpy()
        y_array = y.to_numpy()
        if num_days_ahead == 0:
            y_array = y_array[0]
        #Add to our samples
        x_vect.append(x_array)
        y_vect.append(y_array)
        #Increment
        x_start = x_start +1
        x_end = x_end + 1
        y_start = y_start + 1
        y_end = y_end + 1
    #Finally, convert to a numpy array 
    x_vect = np.array(x_vect)
    y_vect = np.array(y_vect)
    print(len(x_vect))
    print(len(y_vect))
    print(x_vect[0])
    print(y_vect[0])
    print(x_vect.shape)
    print(y_vect.shape)
    return x_vect, y_vect 











#df_test['Btime'].iloc[0]

def one_single():
    import npp_c_cali
    df = npp_c_cali.return_data()
    columns_keep = get_keep_columns(single_data_streams)
    #Only keep certain columns
    
    df = df[columns_keep]
    df = df.dropna()
    #Line gets rid of dropped data 
    df = df.reset_index(drop=True)
    #print(df.describe())
    #print(df["Date_datetime"].iloc[0])
    #print(list(df.columns))


    time_steps = 200
    #Want to predict starting one day ahead 
    days_ahead = 1
    #Only want to predict one day
    num_days_ahead = 0

    #x_vect, y_vect = time_slice_naive(df, time_steps, days_ahead, num_days_ahead)

    x_vect, y_vect = time_slice_continuous(df, time_steps, days_ahead, num_days_ahead)

    #print(df.loc[796:796, :])

#one_single()



def prep_for_machine_learning():

    pass
    #Here you need to one-hot encode (including categorical like sitename), normalize, weight initialize, etc. 
    #Might be careful of the Sitename variable and any other strings and how you might need to convert them. 



#Dummy variables - maybe list column names before conversion. 
#pd.get_dummies(data,prefix=["gen","city"],columns=["gender","city"])



# dataset_1 = {
#     "datasets": ["npp_c_cali", "npp_c_grav"],
#     "input_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
#     "output_dataset": ["npp_c_cali"],
#     "output_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
#     "input_slices_days": 7,
#     "output_slices_days": 1,
#     "output_offset_days": 1,
#     "task_type": "regression",
#     "clean_method": "drop",
#     "concat_key": "Date_datetime"
# }



dataset_1 = {
    "datasets": ["npp_c_cali", "npp_c_grav"],
    "input_fields": {
        "npp_c_cali": {
            "Air_TempC_Avg": "Air_TempC_Avg",
            "Air_TempC_Max": "Air_TempC_Max"
        },
        "npp_c_grav": {
            "Relative_Humidity_Avg": "Relative_Humidity_Avg",
            "Relative_Humidity_Max": "Relative_Humidity_Max"
        },
    },
    "output_dataset": ["npp_c_cali"],
    "output_fields": {
        "npp_c_cali": {
            "Air_TempC_Avg": "Air_TempC_Avg",
            "Air_TempC_Max": "Air_TempC_Max"
        },
        "npp_c_grav": {
            "Relative_Humidity_Avg": "Relative_Humidity_Avg",
            "Relative_Humidity_Max": "Relative_Humidity_Max"
        },
    },
    "input_slices_days": 200,
    "output_slices_days": 1,
    "output_offset_days": 1,
    "task_type": "regression",
    #"clean_method": "drop",
    "clean_method": "fill",
    "concat_key": "Date_datetime"
}

def get_input_output_fields(dataset_object):
    i_fields = dataset_object["input_fields"]
    o_fields = dataset_object["output_fields"]
    if isinstance(i_fields, dict):
        send_i_fields = []
        for dataset_name in list(i_fields.keys()):
            send_i_fields = send_i_fields + list(i_fields[dataset_name].values())
    else:
        send_i_fields = i_fields
    if isinstance(o_fields, dict):
        send_o_fields = []
        for dataset_name in list(o_fields.keys()):
            send_o_fields = send_o_fields + list(o_fields[dataset_name].values())
    else:
        send_o_fields = o_fields
    return send_i_fields, send_o_fields

    


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
def time_slice(dataset_object, df):
    input_slices_days = dataset_object["input_slices_days"]
    output_slices_days = dataset_object["output_slices_days"]
    output_offset_days = dataset_object["output_offset_days"]

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
    #3. 

    print(df.describe())
    print(list(df.columns))
    print("--------------")

    input_fields, output_fields = get_input_output_fields(dataset_object)
    print(input_fields)
    print(output_fields)
    print("--------------")

    x_vect, y_vect = time_slice(dataset_object, df)




create_dataset_from_dataset_object(dataset_1)

# DATASETS
# (Need preprocessing per field)? 
# datasets = (list) - list of dataset names 
# input_fields: fields = either a list of field names OR
#         a dict keyed by dataset name 
#             sub dict: dataset_field (key), field_name mapping (value)
# output_dataset: list, or value (same) to say they are same as input 
# output_fields: (same as input)
# input_time_slices: # of days back
# output_time_slices: # of days forward or N/A (prediction),
# output_offset = ,
# type: prediction or regression 
# _date_boundary? 

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


# def create_merged_df(dataset_object):
#     whole_df = pd.DataFrame()
#     dataset_list = dataset_object["datasets"]
#     concat_key = dataset_object["concat_key"]
#     input_fields = dataset_object["input_fields"]
#     i = 0
#     for dataset in dataset_list:
#         #NEED TO CHANGE THIS EVENTUTALLY 
#         cols_use = input_fields
#         prefix_string = dataset+"_"
#         prefix_concat = prefix_string+concat_key
#         cols_grab = cols_use.copy()
#         cols_grab.append(concat_key)
#         module = importlib.import_module(dataset, package=None)
#         #Get the dataframe from the module
#         df = module.return_data()
#         #Only keep the columns we want
#         df = df[cols_grab]
#         df = df.add_prefix(prefix_string)
#         df = df.rename(columns={prefix_concat: concat_key})
#         if i > 0:
#             whole_df = pd.merge(whole_df, df, on=concat_key)
#         else:
#             whole_df = df
#         i = i+1
#     return df 


# #Attempts to take only continuous values
# def time_slice_continuous(df, time_steps, days_ahead, num_days_ahead): 
#     num_rows = len(df)
#     x_vect = []
#     y_vect = []
#     x_start = 0
#     x_end = time_steps-1
#     y_start = time_steps+days_ahead
#     y_end = y_start+num_days_ahead
#     #Get x and y values indexed properly. 
#     while y_end < num_rows-1:
#         append_flag = 1
#         #Get the proper slice 
#         x = df.loc[x_start:x_end, :]
#         y = df.loc[y_start:y_end, :]
#         #Get last row of x and y
#         first_x = x["Date_datetime"].iloc[0]
#         last_x = x["Date_datetime"].iloc[-1]
#         first_y = y["Date_datetime"].iloc[0]
#         last_y = y["Date_datetime"].iloc[-1]

#         #Get rid of continuity errors caused by NaNs 
#         #If last row of x not time_steps above first row of x, continue
#         if first_x + timedelta(days=time_steps) < last_x:
#             append_flag = 0
#         #If y not days_ahead of x, continue
#         if last_x + timedelta(days=days_ahead) < first_y:
#             append_flag = 0
#         #If last y not num_days_ahead of x, continue 
#         if first_y + timedelta(days=num_days_ahead) < last_y:
#             append_flag = 0

#         if append_flag:
#             #Change from a dataframe to the vector we want 
#             x_array = x.to_numpy()
#             y_array = y.to_numpy()
#             if num_days_ahead == 0:
#                 y_array = y_array[0]
#             #Add to our samples
#             x_vect.append(x_array)
#             y_vect.append(y_array)
#             #Increment
#             x_start = x_start +1
#             x_end = x_end + 1
#             y_start = y_start + 1
#             y_end = y_end + 1
#     #Finally, convert to a numpy array 
#     x_vect = np.array(x_vect)
#     y_vect = np.array(y_vect)
#     print(len(x_vect))
#     print(len(y_vect))
#     print(x_vect[0])
#     print(y_vect[0])
#     print(x_vect.shape)
#     print(y_vect.shape)
#     return x_vect, y_vect 