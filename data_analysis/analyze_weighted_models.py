#Help from:
#https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas 
#https://www.geeksforgeeks.org/how-to-iterate-over-files-in-directory-using-python/ 

import pandas as pd
import matplotlib.pyplot as plt 
import json 
import os 
import scipy.stats as stats 
import seaborn as sn

#Group by Documentation
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html 

# colnames=['TIME', 'X', 'Y', 'Z'] 
# user1 = pd.read_csv('dataset/1.csv', names=colnames, header=None)
#https://www.geeksforgeeks.org/how-to-plot-multiple-data-columns-in-a-dataframe/ 



groups = {
    "ae": ["E", "H", "L", "S", "U", "X", "Z", "AC"],
    "lstm": ["A", "B", "C", "D", "F", "G", "I", "J",
                "M", "N", "Q", "T", "V", "W", "Y", "AA", "AB", "AD"
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
    "prediction": [
            "version",
            "location_scheme",
            "datastream_scheme",
            "l_combo",
            "ds_combo",
            "input_days",
            "output_days",
            "loss",
            "mse",
            "binary_accuracy",
            "precision",
            "recall",
            "true_positives",
            "true_negatives",
            "false_positives",
            "false_negatives",
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


def return_aggregate_metrics_dict():
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
        },
        "prediction": {
            "letter": [],
            "phase_letter": [],
            "mean_mse": [],
            "min_mse": [],
            "max_mse": [],
            "stdev_mse": [],
            "mean_binary_accuracy": [],
            "min_binary_accuracy": [],
            "max_binary_accuracy": [],
            "stdev_binary_accuracy": [],
            "mean_training_time": [],
            "mean_num_epochs": [],
            "location_scheme": [],
            "datastream_scheme": [],
            "num_experiments": [],
        }
    }
    return aggregate_metrics


#Calculated the weighted metric 
def calc_weighted_metric(df, input_output_csv, total_outputs, prediction=False):
    #print(df["dataset_name"])
    new_dataset_name = df["dataset_name"].item()
    i_o_csv = input_output_csv.loc[input_output_csv["dataset_name"] == new_dataset_name]
    print(i_o_csv["output_size"])
    output_size = i_o_csv["output_size"].item()
    weighting = output_size/total_outputs
    #And the mse.
    if prediction:
        metric = "binary_accuracy"
    else:
        metric = "mse"

    value_metric = df[metric].item()
    weighted_metric = value_metric*weighting
    return weighted_metric

#This is ONE variation. 
def load_and_weight(phase, letter, curr_sep_dict, curr_sep_kind, input_var, output_var, exp_var, input_output_csv, total_outputs, prediction=False):
    location_combo = [*range(0, 16)]
    datastream_combo = [*range(0, 5)]
    exp_name = f"{phase}_{letter}_exp{exp_var}"
    #Try to load in the whole df for this phase and letter 
    metrics_path = f"main_metrics/phase_{phase}/{phase}_{letter}main_metrics.csv"
    if prediction:
        cols = col_names["prediction"]
    else:
        cols = col_names["lstm"]
    whole_df = pd.read_csv(metrics_path, names=cols)
    #Restrict the df to our particular variation
    df_restrict = whole_df[(whole_df['input_days']==input_var) & (whole_df['output_days']==output_var) & (whole_df['experiment_name']==exp_name)]
    # print(phase)
    # print(letter)
    # print(input_var)
    # print(output_var)
    # print(exp_name)
    # print(df_restrict.head())
    #CHANGE
    if curr_sep_kind == "all_all":
         weighted_mse = calc_weighted_metric(df_restrict, input_output_csv, total_outputs, prediction=prediction)
    elif curr_sep_kind == "one_all":
        weighted_sum = 0 
        for ds_index in datastream_combo:
            new_df = df_restrict[df_restrict['ds_combo']==ds_index]
            if not new_df.empty:
                weighted_sum = weighted_sum + calc_weighted_metric(new_df, input_output_csv, total_outputs, prediction=prediction)
        weighted_mse = weighted_sum
    elif curr_sep_kind == "all_one": 
        weighted_sum = 0 
        for l_index in location_combo:
            new_df = df_restrict[df_restrict['l_combo']==l_index]
            if not new_df.empty:
                weighted_sum = weighted_sum + calc_weighted_metric(new_df, input_output_csv, total_outputs, prediction=prediction)
        weighted_mse = weighted_sum
    elif curr_sep_kind == "one_one":
        weighted_sum = 0 
        for l_index in location_combo:
            for ds_index in datastream_combo:
                new_df = df_restrict[(df_restrict['l_combo']==l_index) & (df_restrict['ds_combo']==ds_index)]
                if not new_df.empty:
                    weighted_sum = weighted_sum + calc_weighted_metric(new_df, input_output_csv, total_outputs, prediction=prediction)
        weighted_mse = weighted_sum

    #Add info to dict
    curr_sep_dict["letter"].append(letter)
    curr_sep_dict["input_days"].append(input_var)
    curr_sep_dict["output_days"].append(output_var)
    curr_sep_dict["experiment_name"].append(exp_name)
    curr_sep_dict["weighted_metric"].append(weighted_mse)

    

def get_all_weighted_variations(phase, letter, curr_sep_kind, total_outputs, prediction=False):
    variation_dict = {
        "letter": [],
        "input_days": [],
        "output_days": [],
        "experiment_name": [], 
        "weighted_metric": []
    }
    input_output_csv = pd.read_csv("inputs_outputs/full_inputs_outputs.csv")
    input_days = [30, 60]
    output_days = [1, 7]
    scaling_factors = [8, 32, 64]
    
    for input_var in input_days:
        for output_var in output_days:
            for exp_var in scaling_factors:
                load_and_weight(phase, letter, variation_dict, curr_sep_kind, input_var, output_var, exp_var, input_output_csv, total_outputs, prediction=False)
    
    #Then save 
    save_folder = f"{phase}_analysis/combo_models/"
    if not os.path.exists(save_folder):
        os.makedirs(save_folder)
    save_name = f"{letter}_combos_weighted.csv"

    save_path = save_folder+save_name

    df = pd.DataFrame(variation_dict)
    df.to_csv(save_path, index=False)


def get_best_weighted_model_per_organization(phase, total_outputs, prediction=False):
    #Letters
    separate_letters = ['D', 'I']
    separate_datastreams_all_locations = ["C", "F", "Q", "AA", "AI"]
    all_datastreams_separate_locations = ["B", "J", "M", "V", "AF"]
    all_datastreams_all_locations = ["A", "G", "N", "T", "W", "Y", "AB", "AD", "AG", "AJ"]


    #Alltogether now 
    separation_schemes = [separate_letters, separate_datastreams_all_locations, all_datastreams_separate_locations, all_datastreams_all_locations]
    separation_kinds = ["one_one", "one_all", "all_one", "all_all"]

    #For each separation scheme: 
    for i in range(0, len(separation_schemes)):
        curr_sep_scheme = separation_schemes[i]
        curr_sep_kind = separation_kinds[i]
        for letter in curr_sep_scheme:
            get_all_weighted_variations(phase, letter, curr_sep_kind, total_outputs, prediction=prediction)

    

phase = "2"
total_outputs = 209 
prediction = False
get_best_weighted_model_per_organization(phase, total_outputs, prediction=prediction)
    




