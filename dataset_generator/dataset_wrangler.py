import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 
import dataset_generator
import model_generator

datasets_base_path = "/home/marz/Documents/ai_research/jornada/datasets/"
experiments_base_path = "/home/marz/Documents/ai_research/jornada/experiments/"

#Start with JUST One - NPP 
npp_sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
csis_sites = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
npp_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']
#csis_named_sites = ['csis_block_1', 'csis_block_2', 'csis_block_3', 'csis_block_4', 'csis_block_5', 'csis_block_6', 'csis_block_7', 'csis_block_8', 'csis_block_9', 'csis_block_10', 'csis_block_11', 'csis_block_12', 'csis_block_13', 'csis_block_14', 'csis_block_15']
csis_named_sites = []
all_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west', 'csis_block_1', 'csis_block_2', 'csis_block_3', 'csis_block_4', 'csis_block_5', 'csis_block_6', 'csis_block_7', 'csis_block_8', 'csis_block_9', 'csis_block_10', 'csis_block_11', 'csis_block_12', 'csis_block_13', 'csis_block_14', 'csis_block_15']
input_days = [7, 30, 60, 200, 365]
output_days = [1, 5, 7, 10, 30]
separate_data_streams = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    #"wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max'],
    "wind_direction": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
}

#"wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],

#Need to fix or handle the missing data here!!! 
#TOMORROW! 
separate_stream_headers = ["temp_hum", "rain", "wind_speed", "wind_direction"]
all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max']
#all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', 'Ppt_mm_Tot', 'WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WinDir_mean_Resultant', 'WinDir_Std_Dev']


#Takes list of datasets, list of fields. Assumes each dataset gets same fields 
def all_but(site_name, larger_list):
    new_list = larger_list.copy()
    if isinstance(site_name, list):
        for item in site_name:
            new_list.remove(site_name)
    else:
        new_list.remove(site_name)
    return new_list

#Get datasets from particular keywords 
def get_datasets_list(datasets):
    dataset_list = []
    #First, make a dataset list. 
    for single_dataset in datasets: 
        if single_dataset == "ALL":
            dataset_list = dataset_list + npp_named_sites + csis_named_sites
        elif single_dataset == "ALL_NPP":
            dataset_list = dataset_list + npp_named_sites
        elif single_dataset == "ALL_CSIS":
            dataset_list = dataset_list + csis_named_sites
        else:
            dataset_list.append(single_dataset)
    #Gets rid of duplicate list entries, if applicable. 
    dataset_list = [*set(dataset_list)]
    return dataset_list

#Get datastreams from particular keywords
def get_datastreams_list(fields):
    fields_list = []
    for field in fields:
        if field == "ALL":
            fields_list = fields_list + all_data_streams
        elif field in separate_stream_headers:
            fields_list = fields_list + separate_data_streams[field]
        else:
            fields_list.append(field)
    fields_list = [*set(fields_list)]
    return fields_list

#Make the dataset descriptor fields dictionary 
def make_single_fields_dict(datasets, fields):
    main_dict = {} 
    dataset_list = get_datasets_list(datasets)
    fields_list = get_datastreams_list(fields)
    sub_dict = {}
    for field in fields_list:
        sub_dict[field] = field
    for single_dataset in dataset_list:
        main_dict[single_dataset]  = sub_dict
    return main_dict



# datasets = ["ALL"]
# #fields = ["temp_hum"]
# fields = ["temp_hum", "rain", 'WS_ms_300cm_Avg']
#make_single_fields_dict(datasets, fields)

# new_sites = all_but(["npp_c_cali"], npp_named_sites)
# print(new_sites)
# print(len(new_sites))

#And this is just for regression >_<. 
#1 - ALL to ALL
#2 - ONE to ONE
#3 - ALL to ONE 
#4 - ONE to ALL 

#Data_Separation (ds)
#1 - ALL to ALL (All data streams predict to all data streams)
#2 - ONE to ONE (One data stream predicts to the same data stream)
#3 - ALL to ONE (All (other) data streams predict to the remaining data stream)
#4 - ONE to ALL (One data stream predicts to all (other) data streams )

#Locations (l)
#1 - ALL to ALL - (All sites predict to all sites)
#2 - ONE to ONE - (One site predicts to the same site)
#3 - ALL to ONE - (All sites predict to one site)
#4 - ONE to ALL - (One site predicts to all other sites)

#dataset name is therefore simple_reg_weather.v[1+].ds[1-4].l[1-4].combo[INDEX].idays[index].odays[INDEX]


#Need an auto-dictionary creator for 
#input datasets, input fields
#output datasets, output fields 

#9 types of experiments - probably should have 9ish functions. 
#Break down to whether data stream is all together or broken up
#Break down if all-to-all, one-to-one, all-to-one 
#Set a large number of epochs and incorporate early stopping, I think. 
# Regression Models
#This is a good start 
#Data ALL together 
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 
#ONE data stream to ONE data stream 
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 
#ALL OTHER data streams to ONE data stream (maybe pick subset? -- for later )
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 
##ONE data streams to ALL other data stream (maybe pick subset? -- for later )
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 

#Data all together, all sites predict all weather for all sites. 
def return_non_varying_data_descriptor():
    main_dict = {}
    main_dict["normalize"]= True
    main_dict["task_type"]= "regression"
    main_dict["clean_method"] = "fill"
    main_dict["concat_key"] = "Date_datetime"
    main_dict["dataset_folder_path"] = datasets_base_path
    main_dict["output_offset_days"] = 1
    main_dict["categorical"]= []
    return main_dict

def create_dataset_name(ds, l, combo, idays, odays):
    version = 1
    name = "simple_reg_weather.v"+str(version)+".ds"+str(ds)+".l"+str(l)+".combo"+str(combo)+".idays"+str(idays)+".odays"+str(odays)
    return name

#dataset name is therefore 
#simple_reg_weather.v[1+].ds[1-4].l[1-4].combo[INDEX].idays[index].
#odays[INDEX]


#Need to add datasets, input fields, output fields, input slices days, output slices dats, and dataset name 
def ds1l1():
    #params 
    datasets = ["ALL"]
    fields = ["ALL"]
    descriptors_list = []
    #Get base 
    dataset_dict = return_non_varying_data_descriptor()
    datasets_list = get_datasets_list(datasets)
    dataset_dict["datasets"] = datasets_list
    #both_dicts = make_single_fields_dict(datasets, fields)
    overall_fields = get_datastreams_list(fields)
    dataset_dict["input_fields"] = overall_fields
    dataset_dict["output_fields"] = overall_fields
    #Don't need to modulate over input and output fields here. Just inputs and ouputs. 
    for idays_index in input_days:
        for odays_index in output_days:
            new_dict = dataset_dict.copy()
            new_dict["input_slices_days"] = idays_index
            new_dict["output_slices_days"] = odays_index
            name = create_dataset_name(1, 1, 0, idays_index, odays_index)
            new_dict["dataset_name"] = name
            descriptors_list.append(new_dict)
            new_dict = {}
    return descriptors_list

descriptors_list = ds1l1()
print(descriptors_list[0])

# datasets = ["ALL"]
# fields = ["ALL"]
# both_dicts = make_single_fields_dict(datasets, fields)
# print(both_dicts)

dataset_generator.create_dataset_from_dataset_object(descriptors_list[0])

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
#     "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
# }















