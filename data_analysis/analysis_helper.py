#Help from:
#https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas 
#https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/ 

import pandas as pd
import matplotlib.pyplot as plt 
import json 
import os 

import analyze_aggregate_metrics
import analyze_individual_metrics
import analyze_separate_schemes 


groups = {
    "ae": ["E", "H", "L", "S", "U", "X", "Z", "AC"],
    "lstm": ["A", "B", "C", "D", "F", "G", "I", "J",
                "M", "N", "Q", "T", "V", "W", "Y", "AA", "AB" "AD",
                ]

}

col_names = {
    "lstm": [
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
    ],

    "ae": [
            "version",
            "location_scheme",
            "datastream_scheme",
            "l_combo",
            "ds_combo",
            "input_days",
            "output_days",
            "loss",
            "mse",
            "dataset_size",
            "training_time",
            "experiment_name",
            "dataset_name",
            "epochs"
        ]
}



aggregate_metrics = {
    "lstm": {
        "letter": [],
        "phase_letter": [],
        "mean_mse": [],
        "min_mse": [],
        "max_mse": [],
        "stdev_mse": [],
        "mean_mape": [],
        "min_mape": [],
        "max_mape": [],
        "stdev_mape": [],
        "mean_mae": [],
        "min_mae": [],
        "max_mae": [],
        "stdev_mae": [],
        "mean_training_time": [],
        "mean_num_epochs": [],
        "location_scheme": [],
        "datastream_scheme": [],
        "num_experiments": [],
    },

    "ae":  {
        "letter": [],
        "phase_letter": [],
        "mean_mse": [],
        "min_mse": [],
        "max_mse": [],
        "stdev_mse": [],
        "mean_training_time": [],
        "mean_num_epochs": [],
        "location_scheme": [],
        "datastream_scheme": [],
        "num_experiments": [],
    }
}

network_1_letters = ["A", "B", "C", "D"]
network_2_letters = ["E", "F", "G", "H", "I", "J", "L", "M", "N", "Q"]
network_3_letters = ["S", "T", "U", "V", "W", "X", "Y", "Z", "AA", "AB"]
network_4_letters = ["E", "F", "L", "M", "AC", "AD"]

networks_list = [network_1_letters, network_2_letters, network_3_letters, network_4_letters]


one_one_letters = ["D", "H", "I"]
one_all_letters = ["C", "E", "F", "Q", "Z", "AA"]
all_one_letters = ["B", "J", "L", "M", "U", "V"]
all_all_letters = ["A", "G", "N", "S", "T", "W", "X", "Y", "AB", "AC", "AD"]

separation_scheme_list = [one_one_letters, one_all_letters, all_one_letters, all_all_letters]
separation_scheme_kinds = ["one_one", "one_all", "all_one", "one_one" ]



def minimum_comparison_models(phase):
    file_path_start = f"main_metrics/"
    #Have kinda a funky way of doing this. But I think it'll work. 
    analyze_separation_schemes.get_min_per_organization(file_path_start, [phase], "lstm")

def aggregate_metrics(phase):
    file_path = f'main_metrics/phase_{phase}/'
    scheme = "lstm"
    analyze_aggregate_metrics.save_metrics(phase, scheme, file_path)

def get_correct_letters(sep_scheme, group):
    correct_letters = []
    for letter in sep_scheme:
        if letter in groups[group]:
            correct_letters.append(letter)
    return correct_letters

def test_and_table(sep_kind, correct_letters, phase):
        #Get the table
        file_path_1 = f"main_metrics/phase_{phase}/"
        analyze_separation_schemes.table_letters(sep_kind, correct_letters, file_path_1, phase, "lstm")
        #Get the test 
        analyze_separation_schemes.test_letters(sep_kind, correct_letters, file_path_1, phase, "lstm")


#def get_min_models_per_network_type(sep_kind, correct_letters, phase):



phases = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14"]
def run_basic_analysis(phases):
    #For each slate of experiments 
    for phase in phases:
        #First, get the aggregate metrics on the whole thing 
        aggregate_metrics(phase)
        #We also want C 
        minimum_comparison_models(phase)
        #Then get the metrics per separation scheme:
        #Will need to make sure this saves correctly 
        for i in range(0, len(separation_scheme_list)):
            #Get the separation scheme letters 
            sep_scheme = separation_scheme_list[i]
            #Get the separation kind name
            sep_kind = separation_scheme_kinds[i]
            #Limit to only LSTM letters 
            correct_letters = get_correct_letters(sep_scheme, "lstm")
            #Test and Table (A I and II)
            test_and_table(sep_kind, correct_letters, phase)
            #Now for B -- We will need to break it up by Network Type
            #First, find the model with the minimum mean mse and min min mse 
            #But we want to find this for each network, which is a trifle trickier 
            #Load in the 


#But we need to find a per-separation scheme, per-network ad-hoc analysis 

#This is a B thing - may want to do it manually? 
#I think we very much do want to do this manually
#It creates the graphs for that letter, and then also finds the minumum
#Model for the main metrics 

def get_best_graphs(phase, letter):
    pass 


  