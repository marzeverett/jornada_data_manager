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


#Let's take out min Wind, since it is almost always 0. 
#datasets_base_path = "/home/maryeverett/Documents/ai_research/jornada_data_manager/experiments/generated_files/datasets/"

#These will be set in the function 
parameters_dict = {
    "phase_path": "generated_files/phase_1_ae_individual/",
    "input_days": [30, 60],
    "output_days": [1, 7],
    "target_model": "time_regression",
    "base_dataset_name": "simple_reg_weather_ae",
    "list_of_base_sets": [],
    "ae_models": [],
    "ae_prev_names": []
}

static_parameters_dict = {
    "phase_path": "generated_files/phase_1_ae_individual/",
    "input_days": [30, 60],
    "output_days": [1, 7],
    "target_model": "time_regression",
    "base_dataset_name": "simple_reg_weather_ae",
    "list_of_base_sets": [],
    "ae_models": [],
    "ae_prev_names": []
}


datasets_base_path = "generated_files/datasets/"
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

global_data_descriptors_list = []

#Also run a basic experiment. 
#all_data_streams = ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max']
#ALL TO ONE is really our prediction network here. 

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
            dataset_list = dataset_list + npp_named_sites
        else:
            dataset_list.append(single_dataset)
    #Gets rid of duplicate list entries, if applicable. 
    dataset_list = [*set(dataset_list)]
    return dataset_list

#Get datastreams from particular keywords. ALL, or Label of the separate stream 
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
    global parameters_dict
    main_dict = {}
    #main_dict["target_model"] = "time_regression"
    #this is the change from base 1!
    target_model = parameters_dict["target_model"]
    main_dict["target_model"] = target_model
    main_dict["normalize"]= True
    main_dict["task_type"]= "regression"
    main_dict["clean_method"] = "fill"
    main_dict["concat_key"] = "Date_datetime"
    main_dict["dataset_folder_path"] = datasets_base_path
    main_dict["output_offset_days"] = 1
    main_dict["categorical"]= []
    return main_dict


def create_dataset_name(base_name, ds, l, ds_combo, l_combo, idays, odays):
    version = 1
    #Change here 
    name = base_name+".v"+str(version)+".l"+str(l)+".ds"+str(ds)+".l_combo"+str(l_combo)+".ds_combo"+str(ds_combo)+".idays"+str(idays)+".odays"+str(odays)
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
#simple_reg_weather.v[1+].ds[1-4].l[1-4].ds_combo[INDEX].l_combo[INDEX].idays[index].odays[INDEX]

def return_input_output_dict_combo(kind, loc_or_site):
    main_dict = {}
    if loc_or_site == "l":
        all_options = all_named_sites
    elif loc_or_site == "ds":
        all_options = separate_stream_headers 
    if kind == "ALL":
        main_dict["input"] = all_options
        main_dict["output"] = all_options
    elif kind == "ONE": 
        input_list = []
        output_list = []
        for site in all_options:
            input_list.append([site])
            output_list.append([site])
        main_dict["input"] = input_list
        main_dict["output"] = output_list
    else:
        print("Specify ALL or ONE")
    return main_dict


def return_ae_paths(parameters_dict, ae_models, ae_prev_names, ds_index, l_index, ds_combo_index, l_combo_index, idays, odays):
    ae_paths = []
    if "ae_synthesis" in list(parameters_dict.keys()):
        synthesize = parameters_dict["ae_synthesis"]
        #If we synthesize, that means we don't match on index 
        if synthesize == "ds" or synthesize == "l":
            combo_dict = return_input_output_dict_combo("ONE", synthesize)
            #For each ae model listed here 
            for i in range(0, len(ae_models)):
                for combo_index in range(0, len(combo_dict["input"])):
                    if synthesize == "ds":
                        new_ds_index = 1  
                        d_name = create_dataset_name(ae_prev_names[i], new_ds_index, l_index, combo_index, l_combo_index, idays, odays)
                    elif synthesize == "l":
                        new_l_index = 1
                        d_name = create_dataset_name(ae_prev_names[i], ds_index, new_l_index, ds_combo_index, combo_index, idays, odays)
                    first_path = "generated_files/experiments/"+ae_models[i]+"/"+d_name+"/"
                    ae_paths.append(first_path)
        else:
            for i in range(0, len(ae_models)):
                d_name = create_dataset_name(ae_prev_names[i], ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
                first_path = "generated_files/experiments/"+ae_models[i]+"/"+d_name+"/"
                ae_paths.append(first_path)        
    #Otherwise assume we match 
    else:
        for i in range(0, len(ae_models)):
            d_name = create_dataset_name(ae_prev_names[i], ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
            first_path = "generated_files/experiments/"+ae_models[i]+"/"+d_name+"/"
            ae_paths.append(first_path)
    return ae_paths


#This can be called outside 
#l_combo_item is a dictionary of datasets (input/output) 
def generate_data_descriptor(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index, odays, odays_index):
    global parameters_dict
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
    base_dataset_name = parameters_dict["base_dataset_name"]
    name = create_dataset_name(base_dataset_name, ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
    dataset_dict["dataset_name"] = name
    classification = create_dataset_class(ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
    dataset_dict["dataset_class"] = classification
    dataset_dict["input_fields"] = make_single_fields_dict(i_dataset, i_streams)
    dataset_dict["output_fields"] = make_single_fields_dict(o_dataset, o_streams)
    combo_datasets = i_dataset + o_dataset
    dataset_dict["datasets"] = [*set(combo_datasets)]
    ae_models = parameters_dict["ae_models"]
    ae_prev_names = parameters_dict["ae_prev_names"]
    dataset_dict["phase_metrics"] = parameters_dict["phase_metrics"]
    dataset_dict["conv"] = parameters_dict["conv"]
    dataset_dict["conv_and_prev_ae"] = parameters_dict["conv_and_prev_ae"]
    if ae_models != []:
        ae_paths = return_ae_paths(parameters_dict, ae_models, ae_prev_names, ds_index, l_index, ds_combo_index, l_combo_index, idays, odays)
        if ae_paths != []:
            dataset_dict["ae_paths"] = ae_paths
    global_data_descriptors_list.append(dataset_dict)


#Can keep these, probably. 
def generate_level_odays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index):
    global parameters_dict
    output_days = parameters_dict["output_days"]
    for odays_index in range(0, len(output_days)):
        generate_data_descriptor(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, idays, idays_index, output_days[odays_index], odays_index) 
    
def generate_level_idays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index):
    global parameters_dict
    input_days = parameters_dict["input_days"]
    for idays_index in range(0, len(input_days)):
        generate_level_odays(l_combo_item, l_combo_index, l_index, ds_combo_item, ds_combo_index, ds_index, input_days[idays_index], idays_index)

#All sites together predict all data for all sites (1 dataset, not counting i/o or model)
#1 dataset * 15 i/o = 15 datasets 
def generate_base(ds_num, l_num):
    if l_num == 0 and ds_num == 0:
        generate_base_1()
    elif l_num == 1 and ds_num == 0:
        generate_base_2()
    elif l_num == 1 and ds_num == 1:
        generate_base_3()
    elif l_num == 0 and ds_num == 1:
        generate_base_4()


def generate_base_1():
    l = "ALL"
    ds = "ALL"
    l_index = 0
    ds_index = 0
    l_combo_index = 0
    ds_combo_index = 0 
    l_combo_dict = return_input_output_dict_combo(l, "l")
    ds_combo_dict = return_input_output_dict_combo(ds, "ds")
    generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)

#One site predicts all data for one site
#15 datasets * 15 i/o = 225 datasets 
def generate_base_2():
    l = "ONE"
    ds = "ALL"
    l_index = 1
    ds_index = 0
    ds_combo_index = 0
    l_combo_dict = return_input_output_dict_combo(l, "l")
    ds_combo_dict = return_input_output_dict_combo(ds, "ds")
    for l_combo_index in range(0, len(l_combo_dict["input"])):
        generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)

#One sites predicts one data stream for one sites
#15 sites * 4 datastreams * 15 i/o = 900 datasets 
def generate_base_3():
    l = "ONE"
    ds = "ONE"
    l_index = 1
    ds_index = 1
    l_combo_dict = return_input_output_dict_combo(l, "l")
    ds_combo_dict = return_input_output_dict_combo(ds, "ds")
    for l_combo_index in range(0, len(l_combo_dict["input"])):
        for ds_combo_index in range(0, len(ds_combo_dict["input"])):
            generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)

#All sites predict one data stream for all sites 
#4 datastreams * 15 i/o = 60 datasets 
def generate_base_4():
    l = "ALL"
    ds = "ONE"
    l_index = 0 
    ds_index = 1 
    l_combo_index = 0
    l_combo_dict = return_input_output_dict_combo(l, "l")
    ds_combo_dict = return_input_output_dict_combo(ds, "ds")
    for ds_combo_index in range(0, len(ds_combo_dict["input"])):
        generate_level_idays(l_combo_dict, l_combo_index, l_index, ds_combo_dict, ds_combo_index, ds_index)
    

def set_parameters_dict(new_dict):
    global parameters_dict
    for key in list(new_dict.keys()):
        parameters_dict[key] = new_dict[key]



def generate_base_datasets(indexes):
    # for index in indexes:
    #     if index == 1:
    #         generate_base_1()
    #     elif index == 2:
    #         generate_base_2()
    #     elif index == 3:
    #         generate_base_3()
    #     elif index == 4:
    #         generate_base_4()
    generate_base(indexes[0], indexes[1])




##################################################
#Most likely used by outside 
def run_generate(new_dict):
    global parameters_dict
    global global_data_descriptors_list
    parameters_dict = static_parameters_dict
    global_data_descriptors_list = []
    set_parameters_dict(new_dict)
    list_of_base_sets = parameters_dict["list_of_base_sets"]
    generate_base_datasets(list_of_base_sets)
    print(f"Generated {len(global_data_descriptors_list)} dataset descriptors")
    return global_data_descriptors_list

#Generated base dataset descriptors
#print(global_data_descriptors_list[0])
def save_list(new_dict, global_data_descriptors_list):
    global parameters_dict
    global static_parameters_dict
    set_parameters_dict(new_dict)
    #Save base dataset descriptors
    phase_path = parameters_dict["phase_path"]
    pathname = phase_path + "phase1_dataset_descriptors.pickle"
    if not os.path.exists(phase_path):
        os.makedirs(phase_path)
    #Write out the dataset descriptors     
    with open(pathname, "wb") as f:
        pickle.dump(global_data_descriptors_list, f)
    parameters_dict = static_parameters_dict.copy()
    print(f"Successfully saved dataset descriptors to {pathname}")


def run_test(indexes, experiment_1, global_data_descriptors_list):
    #print(global_data_descriptors_list[index])
    for index in indexes:
        dataset_generator.create_dataset_from_dataset_object(global_data_descriptors_list[index])
        experiment_1["dataset_name"] = global_data_descriptors_list[index]["dataset_name"]
        dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.experiment_from_experiment_object(global_data_descriptors_list[index], experiment_1.copy())
        print("Experiment_Descriptor")
        print(experiment_descriptor)
        graph_and_visualize.visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)


#tensorman run --gpu pip3 install pandas 

