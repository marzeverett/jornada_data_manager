import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 
import dataset_generator
import model_generator
import graph_and_visualize 

datasets_base_path = "/home/marz/Documents/ai_research/jornada/datasets/"
experiments_base_path = "/home/marz/Documents/ai_research/jornada/experiments/"

#Start with JUST One - NPP 
npp_sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]
csis_sites = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
npp_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']
#csis_named_sites = []
#csis_named_sites = ['csis_block_1', 'csis_block_2', 'csis_block_3', 'csis_block_4', 'csis_block_5', 'csis_block_6', 'csis_block_7', 'csis_block_8', 'csis_block_9', 'csis_block_10', 'csis_block_11', 'csis_block_12', 'csis_block_13', 'csis_block_14', 'csis_block_15']
all_named_sites = ['npp_c_cali', 'npp_c_grav', 'npp_c_sand', 'npp_g_basn', 'npp_g_ibpe', 'npp_g_summ', 'npp_m_nort', 'npp_m_rabb', 'npp_m_well', 'npp_p_coll', 'npp_p_smal', 'npp_p_tobo', 'npp_t_east', 'npp_t_tayl', 'npp_t_west']

separate_data_streams = {
    "temp_hum": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min'],
    "rain": ['Ppt_mm_Tot'],
    "wind_speed": ['WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min'],
    "wind_direction": ['WinDir_mean_Resultant', 'WinDir_Std_Dev'],
}

l = ["ALL_TO_ALL", "ONE_TO_ONE", "ALL_TO_ONE", "ONE_TO_ALL"]
ds = ["ALL_TO_ALL", "ONE_TO_ONE", "ALL_TO_ONE", "ONE_TO_ALL"]
separate_stream_headers = ["temp_hum", "rain", "wind_speed", "wind_direction"]
all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', 'Ppt_mm_Tot', 'WS_ms_300cm_Avg', 'WS_ms_300cm_Max', 'WS_ms_300cm_Min', 'WS_ms_150cm_Avg', 'WS_ms_150cm_Max', 'WS_ms_150cm_Min', 'WS_ms_75cm_Avg', 'WS_ms_75cm_Max', 'WS_ms_75cm_Min', 'WinDir_mean_Resultant', 'WinDir_Std_Dev']
input_days = [7, 30, 60, 90, 365]
output_days = [1, 7, 30]
global_data_descriptors_list = []

#Also run a basic experiment. 
#all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max']

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
    #Change is here with if statement 
    if sub_dict != {}:
        for single_dataset in dataset_list:
            main_dict[single_dataset]  = sub_dict
    return main_dict

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

def create_dataset_name(ds, l, ds_combo, l_combo, idays, odays):
    version = 1
    name = "simple_reg_weather.v"+str(version)+".l"+str(l)+".ds"+str(ds)+".l_combo"+str(l_combo)+".ds_combo"+str(ds_combo)+".idays"+str(idays)+".odays"+str(odays)
    return name

def create_dataset_class(ds, l, ds_combo, l_combo, idays, odays):
    main_dict = {}
    main_dict["version"] = 1
    main_dict["location_scheme"] = l
    main_dict["datastream_scheme"] = ds
    main_dict["l_combo"] = l_combo
    main_dict["ds_combo"] = ds_combo
    main_dict["input_days"] = idays
    main_dict["output_days"] = odays
    return main_dict

#dataset name is therefore 
#simple_reg_weather.v[1+].ds[1-4].l[1-4].ds_combo[INDEX].l_combo[INDEX].idays[index].
#odays[INDEX]

def return_input_output_dict_combo(kind, loc_or_site):
    main_dict = {}
    if loc_or_site == "l":
        all_options = all_named_sites
    elif loc_or_site == "ds":
        all_options = separate_stream_headers 
    if kind == "ALL_TO_ALL":
        main_dict["input"] = all_options
        main_dict["output"] = all_options
    if kind == "ONE_TO_ONE":
        input_list = []
        output_list = []
        for site in all_options:
            input_list.append([site])
            output_list.append([site])
        main_dict["input"] = input_list
        main_dict["output"] = output_list
    if kind == "ALL_TO_ONE": 
        input_list = []
        output_list = []
        for site in all_options:
            output_list.append([site])
            input_list.append(all_but(site, all_options))
        main_dict["input"] = input_list
        main_dict["output"] = output_list
    if kind == "ONE_TO_ALL": 
        input_list = []
        output_list = []
        for site in all_options:
            input_list.append([site])
            output_list.append(all_but(site, all_options))
        main_dict["input"] = input_list
        main_dict["output"] = output_list
    return main_dict


def generate_data_descriptor(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index, odays, odays_index):
    #global_data_descriptors_list = []
    dataset_dict = return_non_varying_data_descriptor()
    input_list_l = l_combo_item["input"]
    output_list_l = l_combo_item["output"]
    input_list_ds = ds_combo_item["input"]
    output_list_ds = ds_combo_item["output"]
    if isinstance(input_list_l[0], list):
        i_dataset = input_list_l[l_combo_index]
        o_dataset = output_list_l[l_combo_index]
    else:
        i_dataset = input_list_l
        o_dataset = output_list_l
    if isinstance(input_list_ds[0], list):
        i_streams = input_list_ds[ds_combo_index]
        o_streams = output_list_ds[ds_combo_index]
    else:
        i_streams = input_list_ds
        o_streams = output_list_ds
    dataset_dict["input_slices_days"] = idays
    dataset_dict["output_slices_days"] = odays
    name = create_dataset_name(ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
    dataset_dict["dataset_name"] = name
    classification = create_dataset_class(ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
    dataset_dict["dataset_class"] = classification
    dataset_dict["input_fields"] = make_single_fields_dict(i_dataset, i_streams)
    dataset_dict["output_fields"] = make_single_fields_dict(o_dataset, o_streams)
    combo_datasets = i_dataset + o_dataset
    dataset_dict["datasets"] = [*set(combo_datasets)]
    global_data_descriptors_list.append(dataset_dict)



def generate_level_odays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index):
    for odays_index in range(0, len(output_days)):
        generate_data_descriptor(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index, output_days[odays_index], odays_index) 
    
def generate_level_idays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index):
    for idays_index in range(0, len(input_days)):
        generate_level_odays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, input_days[idays_index], idays_index)

def generate_level_ds(l_combo_item, l_combo_index, l_index):
    #data stream params
    for ds_index in range(0, len(ds)):
            ds_combo_dict = return_input_output_dict_combo(ds[ds_index], "ds")
            if isinstance(ds_combo_dict["input"][0], list):
                for ds_combo_index in range(0, len(ds_combo_dict["input"])):
                    generate_level_idays(l_combo_item, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)
            else:
                generate_level_idays(l_combo_item, l_combo_index, l_index, ds_combo_dict, 0, ds_index)

#Pick it back up here. 
def generate_basic_experiments():
    #Modulate location (and combos), datastreams, input days, output days
    #location params 
    #Start with location index: 
    for l_index in range(0, len(l)):
        #dataset_dict = return_non_varying_data_descriptor()
        l_combo_dict = return_input_output_dict_combo(l[l_index], "l")
        if isinstance(l_combo_dict["input"][0], list):
            for l_combo_index in range(0, len(l_combo_dict["input"])):
                generate_level_ds(l_combo_dict, l_combo_index, l_index)
        else:
            generate_level_ds(l_combo_dict, 0, l_index)



experiment_1 = {
    "model":{
        "model_type": "Sequential",
        #Don't include input, code will figure it out. 
        #Don't include output, code will figure it out. 
        "layers": 
            [
                {
                    "type": "LSTM",
                    "num_nodes": 32
                },
                {
                    "type": "Dropout",
                    "percent": 0.2,
                },
            ],
        "final_activation": "relu",
        "loss": "mse",
        #"loss_function": "mean_square_error",
        "optimizer": "adam",
        "batch_size": 32,
        "epochs": 2,
        "test_split": 0.1,
        "validation_split": 0.2,
        "use_multiprocessing": True,
        #"metrics": ["mse"]
        "metrics": ["mse", "mape", "mae"],
    },
    "experiment_folder_path": "/home/marz/Documents/ai_research/jornada/experiments/",
    "experiment_name": "test_experiment_4"
}






#HERE though. 
index = 8969
generate_basic_experiments()
print(global_data_descriptors_list[index])
print(len(global_data_descriptors_list))

for index in range(0, 2):
    experiment_1["experiment_name"] = "test"+str(index)
    experiment_copy = experiment_1.copy()
    print("EXPERIMENT -------------------")
    print(experiment_copy)
    dataset_generator.create_dataset_from_dataset_object(global_data_descriptors_list[index])
    dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.experiment_from_experiment_object(global_data_descriptors_list[index], experiment_copy)
    graph_and_visualize.visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)


#Next steps -
#Final metric reporting sheet for the experiments - all in one 
#(especially since it is going to have 8000 lines)
#ds, loc, 





