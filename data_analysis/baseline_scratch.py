#Help from:
#https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas 
#https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/ 

import pandas as pd
import matplotlib.pyplot as plt 
import json 
import os 
import scipy.stats as stats 
import seaborn as sn
import numpy as np 

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

#sub_dict["df"] = pd.read_csv(f, names=cols)

#This logic looks at the difference in distribution between these 
#two letters 

letter_1 = "A"
letter_2 = "G"
file_path_1 = f'main_metrics/phase_2/2_{letter_1}main_metrics.csv'
file_path_2 = f'main_metrics/phase_2/2_{letter_2}main_metrics.csv'
phase_1 = "4"  
scheme_1 = "lstm"

letter_D = pd.read_csv(file_path_1, names=col_names)
letter_I = pd.read_csv(file_path_2, names=col_names)

D_mse = letter_D["mse"].to_numpy()
I_mse = letter_I["mse"].to_numpy()

diff = np.absolute(D_mse - I_mse)

plt.hist(diff)
plt.xlabel("Absolute Difference")
plt.ylabel("Frequency")
plt.title(f"Histogram of Difference Distribution Between {letter_1} and {letter_2} Model MSE")
plt.show()


# # #All separate
# kind = "table_separate_all"
# letters = ["D", "I"]

# #One datastream_all_locations
# kind = "separate_ds_all_location"
# letters = ["C", "F", "Q", "AA"]

# #All datastreams one location
# kind = "all_ds_separate_location"
# letters = ["B", "J", "M", "V"]


# #All datastreams all locations 
# kind = "all_ds_all_location"
# letters = ["A", "G", "N", "T", "W", "Y", "AD"]



