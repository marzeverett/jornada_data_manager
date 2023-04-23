# Experimental Plan Considerations 

## What to Measure? What Data to Use

### Regression 

1. Site Next-Day Weather 
    Day Prior
    Week Prior
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 
    
2. Site Next-Week Weather 
    Week Prior
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 

3. Site Next-Month Weather
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 

4. Same as above, for soil moisture content 
5. Same as above, for precipitation 

### Classification 

1. Vegetative Cover
2. Animal Presence
3. Dust 


## To Do 
- [ ] Figure out what data streams go where
- [x] Get rid of NaNs/Clean Data
- [ ] Auto script to spatially align data 
- [x] Auto script to pull in and out data streams as needed 
- [ ] Research best LSTM and AE practices
- [x] Auto script for time refactoring
- [ ] Auto script to run models 
- [ ] Exactly how many models to run, figure out how to auto re-run 
- [ ] Auto-save, auto-evaluate models 
- [ ] Auto-save latent space to own datasets as needed 



## Tasks 
Lorem ipsum dolor sit... 

### Base Models (Network 1)
Regression Models
    ALL sites predicts ALL weather for ALL sites
    ONE site predicts ALL weather for ONE site
    ALL sites BROKEN Weather for ONE site
    ALL sites BROKEN Weather for ALL sites
    One site BROKEN weather for ONE Site 

Prediction Models 
    Gap-filled precipitation? 
    Vegetative Cover
    Animal Presence 

### Network 2

### Network 3

### Network 4

### Spatial Models 


### Fields Object:
A fields object can be 1 of 2 things:
1. A list of fields in the dataframe to use (in which cases, all datasets in the dataset list will use all fields). For example: 
    
    ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min']

2. A dictionary, where the first level key corresponds to the dataset name, whose value is a dictionary where keys are field names, mapped to indexes which also field names (they can be same or different, depending on what you want them to correspond to)
   
    {
         "npp_c_cali": {
             "Air_TempC_Avg": "Air_TempC_Avg",
             "Air_TempC_Max": "Air_TempC_Max"
         },
         "npp_c_grav": {
             "Relative_Humidity_Avg": "Relative_Humidity_Avg",
             "Relative_Humidity_Max": "Relative_Humidity_Max"
        }
    }



### Dataset Descriptor
A Dataset a dictionary with the following keys:
"datasets": values is a list of datasets you want to use for input 
"input_fields": a fields object (see above) corresponding to the desired fields for the ML input

"output_fields": a fields object (see above) corresponding to the desired fields for the ML otuput

"input_slices_days": Number of samples (days, in this case) to put into a single input sequence

"output_slices_days": Number of samples (days, in this case) to put into a single output sequence

"output_slices_days": Days of offset from the edge of an input sequence to an output sequence (in most cases, just 1)

"task_type": type os ML task, either regression or prediction 
"clean_method": method of dealing with midding data. "drop" drops it from the dataframe, "fill" fills it in by using surrounding values. In most cases, I would recommend fill. 

"concat_key": The field disparate datasets should be joined on. Mostly Date_datetime in this case. 

"dataset_name": The name to give the dataset 

"cat_codes": indexed to a dictionary of key value pairs where the key is the field name of the categorical variable and the value is a dictionary where the key is mapped to the index of the category 

"normalization_data": A dictionary keyed by field, corresponding to dict of with max and min values keys. 

"reverse_mapping": A dictionary, where the new value of a merged column (after being renamed with it's prefix dataset) corresponds to its original field name. 

"dataset_class": A dictionary, which could have the following keys:
    "location_scheme": the index the location level scheme (0-4) being used 
    "datastream_scheme" the index of the data stream level scheme (0-4) being used
    "l_combo": the index of the combination of input/output locations being used
    "ds_combo": the index of the combination of input/output data streams being used 
    "input_days": the number of input days
    "output_days": the number of output days 
    "version": version of the experiments being run  

Added: 
"x_columns": list of names, in order, of the x columns.
"y_columns": list of names, in order, of the y columns.



## Dataset Result Object 
"x" - x values of dataset object, ready for ML model

"y" - y values of dataset object, ready for ML model

"x_key" - keys of x values for use in dataframe

"y_key" - keys of y values for use in dataframe

After running through the split_training_test function, the following keys are added: 

"x_train" - x values for training set

"x_test" - x values for test set

"y_train" - y values for training set

"y_test" - y values for test set

"x_train_key" - x keys for training set

"x_test_key" - x keys for test set

"y_train_key" - y keys for training set 

"y_test_key" - y keys for test set 

For visualizing, you also get the following: 

"y_unnormalized" - unnormalized y values

"y_train_unnormalized" - unnormalized y values for training set

"y_test_unnormalzied" - unnormalzied y values for test set 


### Experiment Descriptor Object
The experiment descriptor object contains the following keys:

"model" - indexes a dict describing a model object, see below

"experiment_folder_path" - Base path of the experiment folder, must end in "/"

"experiment_name" - name of the experiment


#### Model Object
The model object is a dictionary containing the following keys: 
"model_type": The type of model (for instance, Sequential)

"layers" -  a list of layer objects, see below. You won't bother with defining the input and output layer in this case

"final_activation" - the final activation function of the model (string)

"loss" -  the name of the model loss function (string)

"optimizer" -  the name of the model optimizer

"batch_size" - the batch size, number of samples per batch, of the model

"epochs" - number of epochs the model should run

"test_split" - the split of the test and training set (percent of training set that should be held for test, for instance 0.1)

"validation_split" - the percent of the training set that should be held for validation, for instance 0.2

"use_multiprocessing" - True or False, should mostly be True

"metrics": A list of metric names to use in evaluating and tracking the model and its history 

#### Model layer object
A model layer objectwill always have one key:

"type" - for instance, "LSTM", "Dropout"

"num_nodes" - number of nodes, only where approprate

"percent": percent, only when appropriate. 


### Experiment Result Object 
The experiment result object has the following keys:

"model_history" - a dict of the model history throughout its epochs, indexed by the particular metric or "val_" followed by the particular metric. 

"test_metrics" - the dict of the values of the final metrics on the test set, indexed by metric name

"predictions" - a dict of predictions, indexed by "x", "x_train", and "x_test", corresponding to prediction vectors

"training_time": the amount of time, in seconds, it took to train the model. 

Added: 

"x_pred_unnormalized" - unnormalized x pred values

"x_pred_train_unnormalized" - unnormalized x pred values for training set

"x_pred_test_unnormalzied" - unnormalzied x pred values for test set

"per_feature" - a dict of the metrics per feature, indexed by the metric, which corresponds to a vector of the metric values per feature on the TEST set. For instance, "mse" might be followed by a list of the mse from predicted test values on [temp, humidity, etc]...


### File Names and Locations 
The dataset will be located in its dataset descriptor path/dataset name, and will include the dataset_descriptor.pickle file and the dataset_results.pickle file

The experiment will be located in its experiment descriptor path/experiment name, and will include the dataset_descriptor.pickle file, dataset_results.pickle file, experiment_descriptor.pickle file,
experiment_results.pickle file, and a folder named "model" containing the files of the best-performing model for its run. 


### Examples

Dataset Descriptor 1
```bash
dataset_1 = {
    "datasets": ["npp_c_cali", "npp_c_grav"],
    "input_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min', "Sitename"],
    "output_fields": ['Air_TempC_Avg', 'Air_TempC_Max', 'Air_TempC_Min', 'Relative_Humidity_Avg', 'Relative_Humidity_Max', 'Relative_Humidity_Min',"Sitename"],
    "categorical": ["Sitename"],
    "normalize": True,
    "input_slices_days": 200,
    "output_slices_days": 1,
    "output_offset_days": 1,
    "task_type": "regression",
    "clean_method": "drop",
    "concat_key": "Date_datetime",
    "dataset_name": "test_dataset_1",
    "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
}
```

Dataset Descriptor 2
```bash
dataset_1 = {
    "datasets": ["npp_c_cali", "npp_c_grav"],
    "input_fields": {
        "npp_c_cali": {
            "Air_TempC_Avg": "Air_TempC_Avg",
            "Air_TempC_Max": "Air_TempC_Max"
        },
        "npp_c_grav": {
            "Relative_Humidity_Avg": "Relative_Humidity_Avg",
            "Relative_Humidity_Max": "Relative_Humidity_Max"
        },
    },
    "output_fields": {
        "npp_c_cali": {
            "Air_TempC_Avg": "Air_TempC_Avg",
            "Air_TempC_Max": "Air_TempC_Max"
        },
        "npp_c_grav": {
            "Relative_Humidity_Avg": "Relative_Humidity_Avg",
            "Relative_Humidity_Max": "Relative_Humidity_Max",
        },
    },
    "categorical": ["Sitename"],
    "normalize": True,
    "input_slices_days": 200,
    "output_slices_days": 1,
    "output_offset_days": 1,
    "task_type": "regression",
    #"clean_method": "drop",
    "clean_method": "fill",
    "concat_key": "Date_datetime",
    "dataset_name": "test_dataset_1",
    "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
}
```

Experiment Descriptor 1
```bash
experiment_1 = {
    "model":{
        "model_type": "Sequential",
        #Don't include input, code will figure it out. 
        #Don't include output, code will figure it out. 
        "layers": 
            [
                {
                    "type": "LSTM",
                    "num_nodes": 31
                },
                {
                    "type": "Dropout",
                    "percent": 0.2,
                },
            ],
        "final_activation": "relu",
        "loss": "mse",
        #"loss_function": "mean_square_error",
        "optimizer": "adam",
        "batch_size": 32,
        "epochs": 2,
        "test_split": 0.1,
        "validation_split": 0.2,
        "use_multiprocessing": True,
        #"metrics": ["mse"]
        "metrics": ["mse", "mape", "mae"],
    },
    "experiment_folder_path": "/home/marz/Documents/ai_research/jornada/experiments/",
    "experiment_name": "test_experiment_1"
}
```

TODO: 
- [x] Figure out how to un-normalize the data for the below suite 
- [x] Create comprehensive visualizations
- [ ] Create an "experiment_group" (maybe auto-generate) key in the experiment descriptor for experiments with the same metrics, which will allow them to be saved to the same csv file. 
https://www.geeksforgeeks.org/how-to-append-pandas-dataframe-to-existing-csv-file/ 
- [ ] Figure out how to define exactly what data and tests to run
- [ ] Figure out how to run these automatically 
- [ ] Nail out phase 1 experiments. 
- [ ] Figure out autoencoder creation and dataset savings from AE.
- [ ] Nail out phase 2 experiments
- [ ] Figure out spatial encodings (Not in this repo)
- [ ] Nail out phase 3 experiments  

Phase 1 Experiments - Base Models, Jornada, no AEs
Phase 2 Experiments - All Jornada data with AE
Phase 3 Experiments - All Spatial Experiments 

1. Site Next-Day Weather 
    Day Prior
    Week Prior
    Month Prior
    Year Prior? 
    Last Month for x amount of years? - ?????
    All the data? 
    
2. Site Next-Week Weather 
    Week Prior
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 

3. Site Next-Month Weather
    Month Prior
    Year Prior? 
    Last Month for x amount of years?
    All the data? 

4. Same as above, for soil moisture content 
5. Same as above, for precipitation 

Regression Models
    ALL sites predicts ALL weather for ALL sites
    ONE site predicts ALL weather for ONE site
    ALL (other) sites BROKEN (into streams) Weather for ONE site
    ALL sites BROKEN Weather for ALL sites
    One site BROKEN weather for ONE Site 

Prediction Models 
    Gap-filled precipitation? 
    Vegetative Cover
    Animal Presence 




#And this is just for regression >_<. 
#1 - ALL to ALL
#2 - ONE to ONE
#3 - ALL to ONE 
#4 - ONE to ALL 

#Data_Separation (ds)
#1 - ALL to ALL (All data streams predict to all data streams)
#2 - ONE to ONE (One data stream predicts to the same data stream)
#3 - ALL to ONE (All (other) data streams predict to the remaining data stream)
#4 - ONE to ALL (One data stream predicts to all (other) data streams )

#Locations (l)
#1 - ALL to ALL - (All sites predict to all sites)
#2 - ONE to ONE - (One site predicts to the same site)
#3 - ALL to ONE - (All sites predict to one site)
#4 - ONE to ALL - (One site predicts to all other sites)

#dataset name is therefore simple_reg_weather.v[1+].ds[1-4].l[1-4].combo[INDEX].idays[index].odays[INDEX]


#Need an auto-dictionary creator for 
#input datasets, input fields
#output datasets, output fields 

#9 types of experiments - probably should have 9ish functions. 
#Break down to whether data stream is all together or broken up
#Break down if all-to-all, one-to-one, all-to-one 
#Set a large number of epochs and incorporate early stopping, I think.


<!-- # Regression Models
#This is a good start 
#Data ALL together 
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 
#ONE data stream to ONE data stream 
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 
#ALL OTHER data streams to ONE data stream (maybe pick subset? -- for later )
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well. 
##ONE data streams to ALL other data stream (maybe pick subset? -- for later )
#     ALL sites predicts ALL weather for ALL sites (straightforward)
#       - repeat for each input and output day mod
#       - only one possible dataset combination (since all)
#       - but can complicate somewhat further by dividing into npp and csis 
#     ONE site predicts ALL weather for ONE site (straightforward)
#       - repeat for each input and output day mod 
#       - repeat for EACH individual site. 
#     ALL (other) sites predict ALL weather for ONE site
#       - repeat for each input and output day mod
#       - repeat for each individual site
#       - Add a zero offset, try and get the same day-weather data as well.  -->