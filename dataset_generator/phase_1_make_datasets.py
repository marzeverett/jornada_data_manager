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

datasets_base_path = "/home/maryeverett/Documents/ai_research/jornada_data_manager/experiments/generated_files/datasets/"
experiments_base_path = "/home/maryeverett/Documents/ai_research/jornada_data_manager/experiments/generated_files/experiments/"


pathname = "generated_files/phase1_dataset_descriptors.pickle"
with open(pathname, "rb") as f:
    dataset_descriptors = pickle.load(f)

index=0
for index in range(0, len(dataset_descriptors)):
    dataset_generator.create_dataset_from_dataset_object(dataset_descriptors[index])

# with open('filename.pickle', 'wb') as handle:
#     pickle.dump(a, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('filename.pickle', 'rb') as handle:
#     b = pickle.load(handle)
# for index in range(0, 2):
#     experiment_1["experiment_name"] = "test"+str(index)
#     experiment_copy = experiment_1.copy()
#     print("EXPERIMENT -------------------")
#     print(experiment_copy)
#     dataset_generator.create_dataset_from_dataset_object(global_data_descriptors_list[index])
#     dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.experiment_from_experiment_object(global_data_descriptors_list[index], experiment_copy)
#     graph_and_visualize.visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)


#Next steps -
#Final metric reporting sheet for the experiments - all in one 
#(especially since it is going to have 8000 lines)
#ds, loc, 



#tensorman run --python3 pip3 install pandas 

#Klugey!
#tensorman =AI_IMAGE_2 run --gpu bash
#In this bash, have to set the user flag if install anything. [pip3 install pkg --user]

#Can run from here or 
#tensorman =AI_IMAGE_2 run --gpu python3 -- ./phase_1_experiments.py 