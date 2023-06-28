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

phase_path = "generated_files/base_1_regression/"



pathname = phase_path + "phase1_dataset_descriptors.pickle"
with open(pathname, "rb") as f:
    dataset_descriptors = pickle.load(f)

start_index=0
for index in range(start_index, len(dataset_descriptors)):
    dataset_generator.create_dataset_from_dataset_object(dataset_descriptors[index])
    