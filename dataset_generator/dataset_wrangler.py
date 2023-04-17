import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 

#Start with JUST One - NPP 
npp_sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
csis_sites = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
input_days = [7, 30, 60, 200, 365]
output_days = [1, 5, 7, 10, 30]
#output_offset_days = [7, 30]

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

#dataset name is therefore simple_reg_weather.ds[1-4].l[1-4].combo[INDEX].idays[index].odays[INDEX]


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

single_data_streams_2 = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    "wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
    "wind_direction": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
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


# data_streams = {
#     "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
#     "rain": ['Ppt_mm_Tot'],
#     "wind_300": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min'],
#     "wind_150": ['WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min'],
#     "wind_75": ['WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
#     "wind_dir": ['WinDir_mean_Resultant', 'WinDir_Std_Dev']
# }
# single_data_streams = {
#     "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
#     "rain": ['Ppt_mm_Tot'],
#     "wind_300": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min'],
#     "wind_150": ['WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min'],
#     "wind_75": ['WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
#     "wind_dir": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
#     "site": ["Sitename"],
#     "datetime": ["Date_datetime"]
# }














