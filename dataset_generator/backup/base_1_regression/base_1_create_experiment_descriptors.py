import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 
import math 

phase_path = "generated_files/base_1_regression/"
datasets_base_path = "generated_files/datasets/"
experiments_base_path = "generated_files/experiments/"
 
# pathname = "generated_files/phase1_dataset_descriptors.pickle"
# with open(pathname, "rb") as f:
#     dataset_descriptors = pickle.load(f)

base_name = "lstm_nodes"

def determine_lstm_nodes_from_dataset_object(dataset_object, scaling_factor):
    input_nodes = dataset_object["x"].shape[-1]
    output_nodes = dataset_object["y"].shape[-1]
    #(this is approximate)
    #num_samples = len(dataset_object["y"])*0.78
    num_samples = len(dataset_object["y"])
    nodes = num_samples / (scaling_factor * (input_nodes + output_nodes))
    nodes = math.ceil(nodes)
    return nodes 

def determine_ae_nodes_from_dataset_object(dataset_object, compression):
    input_nodes = len(dataset_object["x"[-1]])
    final_nodes = input_nodes*compression
    final_nodes = math.ceil(final_nodes)
    return final_nodes

def create_basic_lstm_model_object(num_nodes):
    model = {
            "kind": "LSTM",
            "model_type": "Sequential",
            #Don't include input, code will figure it out. 
            #Don't include output, code will figure it out. 
            "layers": 
                [
                    {
                        "type": "LSTM",
                        "num_nodes": num_nodes
                    },
                    {
                        "type": "Dropout",
                        "percent": 0.2,
                    },
                ],
            "final_activation": "relu",
            "loss": "mse",
            "optimizer": "adam",
            "batch_size": 32,
            "epochs": 100,
            "test_split": 0.1,
            "validation_split": 0.2,
            "use_multiprocessing": True,
            "metrics": ["mse", "mape", "mae"],
            "verbose": False,
        }
    return model 

def create_basic_ae_model_object(num_nodes):
    model = {
        "kind": "AE",
        "model_type": "Sequential",
        "layers": 
            [
                {
                    "type": "Dense",
                    "num_nodes": num_nodes,
                    "activation": "relu",
                    "name": "latent_space"
                },
            ],
        "final_activation": "relu",
        "loss": "mse",
        #"loss_function": "mean_square_error",
        "optimizer": "adam",
        "batch_size": 32,
        "epochs": 100,
        "test_split": 0.1,
        "validation_split": 0.2,
        "use_multiprocessing": True,
        #"metrics": ["mse"]
        "metrics": ["mse"],
        "verbose": False,
    }
    return model 

def create_experiment(num_nodes, dataset_name, kind):
    if kind == "base_lstm":
        model = create_basic_lstm_model_object(num_nodes)
    elif kind == "base_ae":
        model = create_basic_ae_model_object(num_nodes)
    experiment_1 = {
        "model": model,
        "dataset_name": dataset_name,
        "experiment_folder_path": experiments_base_path,
        "experiment_name": base_name+str(num_nodes)
    }
    return experiment_1

def load_dataset_result_from_dataset_descriptor(dataset_descriptor):
    dataset_base_path = dataset_descriptor["dataset_folder_path"]
    full_path = dataset_base_path + dataset_descriptor["dataset_name"]+"/dataset_result.pickle"
    with open(full_path, "rb") as f:
        dataset_result = pickle.load(f)
    return dataset_result
#Name HAS to include dataset or it won't work. 
#nodes = [8, 32, 64]
#nodes = [8]
#These are now scaling factors 
#scaling_factors = [2, 5, 8]
#scaling_factors = [0.1, 0.2, 0.5]
scaling_factors = [8, 32, 64]


d_pathname = phase_path + "phase1_dataset_descriptors.pickle"
with open(d_pathname, "rb") as f:
    dataset_descriptors = pickle.load(f)

experiments = []
for scaling_factor in scaling_factors:
    for dataset in dataset_descriptors: 
        #d_result = load_dataset_result_from_dataset_descriptor(dataset)
        #node_count = determine_lstm_nodes_from_dataset_object(d_result, scaling_factor)
        #This is where we will generate an experiment for a particular node code stream.
        experiments.append(create_experiment(scaling_factor, dataset["dataset_name"], "base_lstm"))
e_pathname = phase_path + "phase1_experiment_descriptors.pickle"
if not os.path.exists(phase_path):
    os.makedirs(phase_path)
with open(e_pathname, "wb") as f:
    pickle.dump(experiments, f)




# experiments = []
# for node_count in nodes:
#     for dataset in dataset_descriptors: 
#         #This is where we will generate an experiment for a particular node code stream.
#         experiments.append(create_experiment(node_count, dataset["dataset_name"], "base_lstm"))

