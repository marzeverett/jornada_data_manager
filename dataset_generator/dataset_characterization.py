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



base_path = "generated_files/"
experiments_base_path = "generated_files/experiments/"

#Start with JUST One - NPP 
npp_sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
npp_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']
all_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']

separate_data_streams = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    "wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max'],
    "wind_direction": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
}

l = ["ALL_TO_ALL", "ONE_TO_ONE", "ALL_TO_ONE", "ONE_TO_ALL"]
ds = ["ALL_TO_ALL", "ONE_TO_ONE", "ALL_TO_ONE", "ONE_TO_ALL"]
separate_stream_headers = ["temp_hum", "rain", "wind_speed", "wind_direction"]
all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', 'Ppt_mm_Tot', 'WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WinDir_mean_Resultant', 'WinDir_Std_Dev']


csv_dict = {
    "Site Name": [],
    "Minimum Date/Time": [], 
    "Maximum Date/Time": [],
    "Features": [],
    #"Geolocation": []
}

def load_in_data(csv_dict):
    for site in npp_named_sites:
        site_path =  f"pickled_datasets/{site}.pkl"
        with open(site_path, "rb") as f:
            dataset = pickle.load(f)
            csv_dict["Site Name"].append(site)
            csv_dict["Minimum Date/Time"].append(dataset["Date"].min())
            csv_dict["Maximum Date/Time"].append(dataset["Date"].max())
            columns = str(list(dataset.columns))
            csv_dict["Features"].append(columns)
    return csv_dict



# csv_dict = load_in_data(csv_dict)
# #print(json.dumps(csv_dict), indent=4)
# csv_dict = pd.DataFrame(csv_dict)
# csv_dict.to_csv("generated_files/site_info_2.csv")
