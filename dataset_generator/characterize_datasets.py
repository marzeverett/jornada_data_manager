import pandas as pd 
import importlib
import numpy as np
from datetime import datetime, timedelta
import os
import json 
import pickle 
os.environ['TF_CPP_MIN_LOG_LEVEL']  = '3'
import tensorflow as tf
tf.get_logger().setLevel('ERROR')
from tensorflow.keras import datasets, layers, models

npp_sites = ["c_cali", "c_grav", "c_sand", "g_basn", "g_ibpe", "g_summ", "m_nort", "m_rabb", "m_well", "p_coll", "p_smal", "p_tobo", "t_east", "t_tayl", "t_west"]

def get_frost_days_per_site():
    for dataset in npp_sites:
        whole_df = pd.DataFrame()
        save_name = "pickled_datasets/npp_"+dataset+".pkl"
        df = pd.read_pickle(save_name)
        #df2 = len(df[df["Courses"]=="Pandas"])
        print("Dataset_Name: ", dataset)
        print("Num Dataset Rows: ", len(df.index))
        print("Num Frost Days: ", len(df[df['Air_TempC_Min'] <= 0]))


def get_storm_days_per_site():
    for dataset in npp_sites:
        whole_df = pd.DataFrame()
        save_name = "pickled_datasets/npp_"+dataset+".pkl"
        df = pd.read_pickle(save_name)
        #df2 = len(df[df["Courses"]=="Pandas"])
        print("Dataset_Name: ", dataset)
        print("Num Dataset Rows: ", len(df.index))
        print("Num Storm Days: ", len(df[df['Ppt_mm_Tot'] >= 10]))

#get_frost_days_per_site()

#get_storm_days_per_site()