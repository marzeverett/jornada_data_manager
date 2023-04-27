import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 
import sys 
sys.path.append("..")
import dataset_generator
import model_generator
import graph_and_visualize 


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

dataset_generator.create_ae_dataset_from_dataset_object(dataset_1)

# #A. 
# #Figure out i_days and o_days here 
# #What datasets will we be using here? 
# #Individual data streams 
# #One per location 
# #l - 2
# #ds - 2 
# #l_combo - 0- 14
# #ds_combo - 0 - 3 
# #One all together 
# #l - 3 
# #ds - 3 
# #l_combo - 0
# #ds_combo - 0 - 3 


# #A.0 - maybe single stream? 
# #A.1 - maybe LSTM AE? 
# #B. LSTM on top is on ALL streams 
# #Have to generate this dataset by saving model outputs 
# #16 datasets 
# #One location at a time, all streams
# #All locations together, all streams 





# def create_dataset_name(ds, l, ds_combo, l_combo, idays, odays):
#     version = 1
#     name = "simple_reg_weather.v"+str(version)+".l"+str(l)+".ds"+str(ds)+".l_combo"+str(l_combo)+".ds_combo"+str(ds_combo)+".idays"+str(idays)+".odays"+str(odays)
#     return name

# def create_dataset_class(ds, l, ds_combo, l_combo, idays, odays):
#     main_dict = {}
#     main_dict["version"] = 1
#     main_dict["location_scheme"] = l
#     main_dict["datastream_scheme"] = ds
#     main_dict["l_combo"] = l_combo
#     main_dict["ds_combo"] = ds_combo
#     main_dict["input_days"] = idays
#     main_dict["output_days"] = odays
#     return main_dict

# def get_dataset_names():
#     pass 

# #Let's take out min Wind, since it is almost always 0. 
# #datasets_base_path = "/home/maryeverett/Documents/ai_research/jornada_data_manager/experiments/generated_files/datasets/"
# phase_path = "generated_files/base_1_regression/"
# datasets_base_path = "generated_files/datasets/"
# experiments_base_path = "generated_files/experiments/"

# #Start with JUST One - NPP 
# npp_sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
# npp_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']
# all_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']

# separate_data_streams = {
#     "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
#     "rain": ['Ppt_mm_Tot'],
#     "wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max'],
#     "wind_direction": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
# }

# l = ["ALL_TO_ALL", "ONE_TO_ONE", "ALL_TO_ONE", "ONE_TO_ALL"]
# ds = ["ALL_TO_ALL", "ONE_TO_ONE", "ALL_TO_ONE", "ONE_TO_ALL"]
# separate_stream_headers = ["temp_hum", "rain", "wind_speed", "wind_direction"]
# all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', 'Ppt_mm_Tot', 'WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WinDir_mean_Resultant', 'WinDir_Std_Dev']
# input_days = [7, 30, 60, 90, 365]
# output_days = [1, 7, 30]
# global_data_descriptors_list = []

# #Also run a basic experiment. 
# #all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max']
# #ALL TO ONE is really our prediction network here. 

# #Takes list of datasets, list of fields. Assumes each dataset gets same fields 
# def all_but(site_name, larger_list):
#     new_list = larger_list.copy()
#     if isinstance(site_name, list):
#         for item in site_name:
#             new_list.remove(site_name)
#     else:
#         new_list.remove(site_name)
#     return new_list

# #Get datasets from particular keywords 
# def get_datasets_list(datasets):
#     dataset_list = []
#     #First, make a dataset list. 
#     for single_dataset in datasets: 
#         if single_dataset == "ALL":
#             dataset_list = dataset_list + npp_named_sites
#         else:
#             dataset_list.append(single_dataset)
#     #Gets rid of duplicate list entries, if applicable. 
#     dataset_list = [*set(dataset_list)]
#     return dataset_list

# #Get datastreams from particular keywords. ALL, or Label of the separate stream 
# def get_datastreams_list(fields):
#     fields_list = []
#     for field in fields:
#         if field == "ALL":
#             fields_list = fields_list + all_data_streams
#         elif field in separate_stream_headers:
#             fields_list = fields_list + separate_data_streams[field]
#         else:
#             fields_list.append(field)
#     fields_list = [*set(fields_list)]
#     return fields_list

# #Make the dataset descriptor fields dictionary 
# def make_single_fields_dict(datasets, fields):
#     main_dict = {} 
#     dataset_list = get_datasets_list(datasets)
#     fields_list = get_datastreams_list(fields)
#     sub_dict = {}
#     for field in fields_list:
#         sub_dict[field] = field
#     #Change is here with if statement 
#     if sub_dict != {}:
#         for single_dataset in dataset_list:
#             main_dict[single_dataset]  = sub_dict
#     return main_dict

# #Data all together, all sites predict all weather for all sites. 
# def return_non_varying_data_descriptor():
#     main_dict = {}
#     main_dict["normalize"]= True
#     main_dict["task_type"]= "regression"
#     main_dict["clean_method"] = "fill"
#     main_dict["concat_key"] = "Date_datetime"
#     main_dict["dataset_folder_path"] = datasets_base_path
#     main_dict["output_offset_days"] = 1
#     main_dict["categorical"]= []
#     return main_dict

# def create_dataset_name(ds, l, ds_combo, l_combo, idays, odays):
#     version = 1
#     name = "simple_reg_weather.v"+str(version)+".l"+str(l)+".ds"+str(ds)+".l_combo"+str(l_combo)+".ds_combo"+str(ds_combo)+".idays"+str(idays)+".odays"+str(odays)
#     return name

# def create_dataset_class(ds, l, ds_combo, l_combo, idays, odays):
#     main_dict = {}
#     main_dict["version"] = 1
#     main_dict["location_scheme"] = l
#     main_dict["datastream_scheme"] = ds
#     main_dict["l_combo"] = l_combo
#     main_dict["ds_combo"] = ds_combo
#     main_dict["input_days"] = idays
#     main_dict["output_days"] = odays
#     return main_dict

# #dataset name is therefore 
# #simple_reg_weather.v[1+].ds[1-4].l[1-4].ds_combo[INDEX].l_combo[INDEX].idays[index].odays[INDEX]

# def return_input_output_dict_combo(kind, loc_or_site):
#     main_dict = {}
#     if loc_or_site == "l":
#         all_options = all_named_sites
#     elif loc_or_site == "ds":
#         all_options = separate_stream_headers 
#     if kind == "ALL":
#         main_dict["input"] = all_options
#         main_dict["output"] = all_options
#     elif kind == "ONE": 
#         input_list = []
#         output_list = []
#         for site in all_options:
#             input_list.append([site])
#             output_list.append([site])
#         main_dict["input"] = input_list
#         main_dict["output"] = output_list
#     else:
#         print("Specify ALL or ONE")
#     return main_dict


# #This can be called outside 
# #l_combo_item is a dictionary of datasets (input/output) 
# def generate_data_descriptor(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index, odays, odays_index):
#     #global_data_descriptors_list = []
#     dataset_dict = return_non_varying_data_descriptor()
#     input_list_l = l_combo_item["input"]
#     output_list_l = l_combo_item["output"]
#     input_list_ds = ds_combo_item["input"]
#     output_list_ds = ds_combo_item["output"]
#     if isinstance(input_list_l[0], list):
#         i_dataset = input_list_l[l_combo_index]
#         o_dataset = output_list_l[l_combo_index]
#     else:
#         i_dataset = input_list_l
#         o_dataset = output_list_l
#     if isinstance(input_list_ds[0], list):
#         i_streams = input_list_ds[ds_combo_index]
#         o_streams = output_list_ds[ds_combo_index]
#     else:
#         i_streams = input_list_ds
#         o_streams = output_list_ds
#     dataset_dict["input_slices_days"] = idays
#     dataset_dict["output_slices_days"] = odays
#     name = create_dataset_name(ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
#     dataset_dict["dataset_name"] = name
#     classification = create_dataset_class(ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
#     dataset_dict["dataset_class"] = classification
#     dataset_dict["input_fields"] = make_single_fields_dict(i_dataset, i_streams)
#     dataset_dict["output_fields"] = make_single_fields_dict(o_dataset, o_streams)
#     combo_datasets = i_dataset + o_dataset
#     dataset_dict["datasets"] = [*set(combo_datasets)]
#     global_data_descriptors_list.append(dataset_dict)


# #Can keep these, probably. 
# def generate_level_odays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index):
#     for odays_index in range(0, len(output_days)):
#         generate_data_descriptor(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index, output_days[odays_index], odays_index) 
    
# def generate_level_idays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index):
#     for idays_index in range(0, len(input_days)):
#         generate_level_odays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, input_days[idays_index], idays_index)

# #All sites together predict all data for all sites (1 dataset, not counting i/o or model)
# #1 dataset * 15 i/o = 15 datasets 
# def generate_base_1():
#     l = "ALL"
#     ds = "ALL"
#     l_index = 0
#     ds_index = 0
#     l_combo_index = 0
#     ds_combo_index = 0 
#     l_combo_dict = return_input_output_dict_combo(l, "l")
#     ds_combo_dict = return_input_output_dict_combo(ds, "ds")
#     generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)

# #One site predicts all data for one site
# #15 datasets * 15 i/o = 225 datasets 
# def generate_base_2():
#     l = "ONE"
#     ds = "ALL"
#     l_index = 1 
#     ds_index = 1
#     ds_combo_index = 0
#     l_combo_dict = return_input_output_dict_combo(l, "l")
#     ds_combo_dict = return_input_output_dict_combo(ds, "ds")
#     for l_combo_index in range(0, len(l_combo_dict["input"])):
#         generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)

# #One sites predicts one data stream for one sites
# #15 sites * 4 datastreams * 15 i/o = 900 datasets 
# def generate_base_3():
#     l = "ONE"
#     ds = "ONE"
#     l_index = 2
#     ds_index = 2
#     l_combo_dict = return_input_output_dict_combo(l, "l")
#     ds_combo_dict = return_input_output_dict_combo(ds, "ds")
#     for l_combo_index in range(0, len(l_combo_dict["input"])):
#         for ds_combo_index in range(0, len(ds_combo_dict["input"])):
#             generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)

# #All sites predict one data stream for all sites 
# #4 datastreams * 15 i/o = 60 datasets 
# def generate_base_4():
#     l = "ALL"
#     ds = "ONE"
#     l_index = 3 
#     ds_index = 3
#     l_combo_index = 0
#     l_combo_dict = return_input_output_dict_combo(l, "l")
#     ds_combo_dict = return_input_output_dict_combo(ds, "ds")
#     for ds_combo_index in range(0, len(ds_combo_dict["input"])):
#         generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)


# def generate_base_datasets():
#     generate_base_1()
#     generate_base_2()
#     generate_base_3()
#     generate_base_4()

# # #Generated base dataset descriptors
# # generate_base_datasets()
# # print(f"Generated {len(global_data_descriptors_list)} dataset descriptors")

# # #Save base dataset descriptors
# # pathname = phase_path + "phase1_dataset_descriptors.pickle"
# # with open(pathname, "wb") as f:
# #     pickle.dump(global_data_descriptors_list, f)
# # print(f"Successfully saved dataset descriptors to {pathname}")
