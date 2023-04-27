import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 

phase_path = "generated_files/base_1_regression/"
datasets_base_path = "generated_files/datasets/"
experiments_base_path = "generated_files/experiments/"
 
# pathname = "generated_files/phase1_dataset_descriptors.pickle"
# with open(pathname, "rb") as f:
#     dataset_descriptors = pickle.load(f)

base_name = "lstm_nodes"

def create_experiment(num_nodes, dataset_name):
    experiment_1 = {
        "model":{
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
        },
        "dataset_name": dataset_name,
        "experiment_folder_path": experiments_base_path,
        "experiment_name": base_name+str(num_nodes)
    }

    return experiment_1

#Name HAS to include dataset or it won't work. 
nodes = [8, 32, 64]
#nodes = [8]


d_pathname = phase_path + "phase1_dataset_descriptors.pickle"
with open(d_pathname, "rb") as f:
    dataset_descriptors = pickle.load(f)

experiments = []
for node_count in nodes:
    for dataset in dataset_descriptors: 
        experiments.append(create_experiment(node_count, dataset["dataset_name"]))

e_pathname = phase_path + "phase1_experiment_descriptors.pickle"
with open(e_pathname, "wb") as f:
    pickle.dump(experiments, f)
