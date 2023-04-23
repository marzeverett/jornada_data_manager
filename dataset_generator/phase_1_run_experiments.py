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
import os


#make a list of our experiments. In this case, we will just have three, and the will only
#vary the number of nodes
#"generated_files/phase1_experiment_descriptors.pickle"
#To start, let's just run one experiment descriptor. 
dataset_base_path = "generated_files/datasets/"
e_pathname = "generated_files/phase1_experiment_descriptors.pickle"
d_pathname = "generated_files/phase1_dataset_descriptors.pickle"
with open(d_pathname, "rb") as f:
    dataset_descriptors = pickle.load(f)

with open(e_pathname, "rb") as f:
    experiment_descriptors = pickle.load(f)

#Start with 8 node experiment only. 
#experiment = experiment_descriptors[0]
start_index = 0
end = len(experiment_descriptors)
#end = len(dataset_descriptors)

for i in range(start_index, end):
    try:
        #get path 
        experiment = experiment_descriptors[i]
        path = dataset_base_path + experiment["dataset_name"] +"/dataset_descriptor.pickle"
        #Load in dataset descriptor 
        with open(path, "rb") as f:
            d_descriptor = pickle.load(f)
            dataset_descriptor, dataset_result, experiment_descriptor, experiment_result = model_generator.experiment_from_experiment_object(d_descriptor, experiment.copy())
            graph_and_visualize.visualize_and_analyze(dataset_descriptor, dataset_result, experiment_descriptor, experiment_result)
    except Exception as e:
        print(f"Error running experiment {i} for reason {e}")
        #Figure this out later 
        # message = f"Error on experiment index {i} for reason {e}"
        # exec_string = f'mpack -s "{message}" alert.txt marzeverett@gmail.com'
        # os.system(exec_string)

print("FINISHED!")
#Figure this out later 
# message = f"Finished! {end} Experiments"
# exec_string = f'mpack -s "{message}" alert.txt marzeverett@gmail.com'
# os.system(exec_string)


#Klugey!
#tensorman =AI_IMAGE_2 run --gpu bash
#In this bash, have to set the user flag if install anything. [pip3 install pkg --user]

#Can run from here or 
#tensorman =AI_IMAGE_2 run --gpu python3 -- ./phase_1_experiments.py 

#Need to cut out verbose-ness

#Change save behavior to experiment_name/dataset_name 