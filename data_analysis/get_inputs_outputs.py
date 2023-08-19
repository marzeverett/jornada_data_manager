#Help from:
#https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas 
#https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/ 
#https://www.geeksforgeeks.org/merge-two-dataframes-with-same-column-names/ 

import pandas as pd
#import matplotlib.pyplot as plt 
import json 
import os 
import scipy.stats as stats 
#import seaborn as sn
import numpy as np 
import pickle 

#Group by Documentation
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html 

# colnames=['TIME', 'X', 'Y', 'Z'] 
# user1 = pd.read_csv('dataset/1.csv', names=colnames, header=None)
#https://www.geeksforgeeks.org/how-to-plot-multiple-data-columns-in-a-dataframe/ 

col_names =  [
            "version",
            "location_scheme",
            "datastream_scheme",
            "l_combo",
            "ds_combo",
            "input_days",
            "output_days",
            "loss",
            "mse",
            "mape",
            "mae",
            "dataset_size",
            "training_time",
            "experiment_name",
            "dataset_name",
            "epochs"
    ]


    #Need for each dataset descriptor
    #going to look like {experiment_name}/{dataset_name}/dataset_result.pkl


def get_inputs_outputs(phase, letter, phase_path):
    #dataset_base_path = "generated_files/datasets/"
    dataset_base_path = "/media/maryeverett/Backup4.0TB/Backup_8_16_23/jornada_data_manager/dataset_generator/generated_files/datasets/"
    d_pathname = phase_path + "phase1_dataset_descriptors.pickle"
    #Load in descriptors 
    with open(d_pathname, "rb") as f:
        dataset_descriptors = pickle.load(f)
    start_index = 0
    end = len(dataset_descriptors)
    dataset_name_list = []
    input_size_list = []
    output_size_list = []
    #Actually run the experiments 
    for i in range(start_index, end):
        try:
            #get path 
            dataset = dataset_descriptors[i]
            dataset_name = dataset["dataset_name"]
            path = dataset_base_path + dataset_name +"/dataset_result.pickle"
            #Load in dataset result 
            with open(path, "rb") as f:
                #Load it in
                d_result = pickle.load(f)
                input_size = d_result["x"].shape[-1]
                output_size = d_result["y"].shape[-1]
                input_size_list.append(input_size)
                output_size_list.append(output_size)
                dataset_name_list.append(dataset_name)
        except Exception as e:
            print(f"Error loading info on dataset {i} for reason {e}")
    #Get dictionary column names 
    dataset_dict = {
        "dataset_name": dataset_name_list,
        "input_size": input_size_list,
        "output_size": output_size_list
    }
    df = pd.DataFrame(dataset_dict)
    df.to_csv(f"{dataset_base_path}/{phase}_{letter}inputs_outputs.csv")

#phase = "2"
#letter = "A"

def get_all_phases():
    phases = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    letters = ['A', 'B', 'C', 'D', 'F', 
    'I', 'L', 'M', 'N', 'Q', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']
    for phase in phases:
        for letter in letters:
            try:
                phase_path = f"/media/maryeverett/Backup4.0TB/Backup_8_16_23/jornada_data_manager/dataset_generator/generated_files/{phase}_{letter}/"
                get_inputs_outputs(phase, letter, phase_path)
            except Exception as e:
                print(f"Couldn't for {phase} and {letter}")
                print(e)
#Get all phases

def make_aggregate_csv():
    phases = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
    letters = ['A', 'B', 'C', 'D', 'F', 
    'I', 'L', 'M', 'N', 'Q', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']
    merged_df = pd.DataFrame()
    for phase in phases:
        for letter in letters:
            try:
                phase_path = f"inputs_outputs/{phase}_{letter}inputs_outputs.csv"
                new_df = pd.read_csv(phase_path)
                if not merged_df.empty:
                    merged_df = pd.concat([merged_df, new_df], axis=0)
                else:
                    merged_df = new_df
            except Exception as e:
                print(f"Couldn't for {phase} and {letter}")
                print(e)
    merged_df.to_csv("inputs_outputs/full_inputs_outputs.csv")
#Need to do a function call 
#get_inputs_outputs

#media/maryeverett/Backup4.0TB/Backup_8_16_23/jornada_data_manager
#/dataset_generator/generated_files/datasets/
#2_A.v1.l0.ds0.l_combo0.ds_combo0.idays30.odays1: No such file or directory

make_aggregate_csv()
