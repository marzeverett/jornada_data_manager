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
- [ x ] Get rid of NaNs/Clean Data
- [ ] Auto script to spatially align data 
- [ x ] Auto script to pull in and out data streams as needed 
- [ ] Research best LSTM and AE practices
- [ ] Auto script for time refactoring
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

### Experiment Schema 

DATASETS
(Need preprocessing per field)? 
datasets = (list) - list of dataset names 
input_fields: fields = either a list of field names OR
        a dict keyed by dataset name 
            sub dict: dataset_field (key), field_name mapping (value)
output_dataset: list, or value (same) to say they are same as input 
output_fields: (same as input)
input_time_slices: # of days back
output_time_slices: # of days forward or N/A (prediction),
output_offset = ,
type: prediction or regression 
_date_boundary? 

EXPERIMENT
Layers: (dict)
    key with num layer index, 
    nodes: number of nodes (value)
    activation_function: activation function
Optimization (Like adam)
Initial LR
Number of epochs?
Early stopping
Metrics (list)
Model save path (do you need multiple? Maybe per number of epochs)
Save values (model history) - what to save 
Save path as well ... 







# dataset_1 = {
#     "datasets": ["npp_c_cali", "npp_c_grav"],
#     "input_fields": {
#         "npp_c_cali": {
#             "Air_TempC_Avg": "Air_TempC_Avg",
#             "Air_TempC_Max": "Air_TempC_Max"
#         },
#         "npp_c_grav": {
#             "Relative_Humidity_Avg": "Relative_Humidity_Avg",
#             "Relative_Humidity_Max": "Relative_Humidity_Max"
#         },
#     },
#     "output_fields": {
#         "npp_c_cali": {
#             "Air_TempC_Avg": "Air_TempC_Avg",
#             "Air_TempC_Max": "Air_TempC_Max"
#         },
#         "npp_c_grav": {
#             "Relative_Humidity_Avg": "Relative_Humidity_Avg",
#             "Relative_Humidity_Max": "Relative_Humidity_Max",
#         },
#     },
#     "input_slices_days": 200,
#     "output_slices_days": 1,
#     "output_offset_days": 1,
#     "task_type": "regression",
#     #"clean_method": "drop",
#     "clean_method": "fill",
#     "concat_key": "Date_datetime",
#     "dataset_name": "test_dataset_1",
#     "model_index": 0, #0-4? 
#     "dataset_folder_path": "/home/marz/Documents/ai_research/jornada/datasets/"
# }

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



### Dataset Object
A Dataset a dictionary with the following keys:
"datasets": values is a list of datasets you want to use for input 
"input_fields": a fields object (see above) corresponding to the desired fields for the ML input
"output_fields": a fields object (see above) corresponding to the desired fields for the ML otuput
"input_slices_days": Number of samples (days, in this case) to put into a single input sequence
"output_slices_days": Number of samples (daus, in this case) to put into a single output sequence
"output_slices_days": Days of offset from the edge of an input sequence to an output sequence (in most cases, just 1)
"task_type": type os ML task, either regression or prediction 
"clean_method": method of dealing with midding data. "drop" drops it from the dataframe, "fill" fills it in by using surrounding values. In most cases, I would recommend fill. 
"concat_key": The field disparate datasets should be joined on. Mostly Date_datetime in this case. 
"dataset_name": The name to give the dataset 
"model_index": The index of the model being run on the dataset. 
"dataset_folder_path": Path of the high-level folder where dataset should be saved to. Should end with a "/"
"cat_codes": indexed to a dictionary of key value pairs where the key is the field name of the categorical variable and the value is a dictionary where the key is mapped to the index of the category 
"normalization_data": A dictionary keyed by field, corresponding to dict of with max and min values keys. 

## Prepared Dataset Object 
"x" - x values of dataset object, ready for ML model 
"y" - y values of dataset object, ready for ML model 
"x_key" - keys of x values for use in dataframe
"y_key" - keys of y values for use in dataframe
"dataset_object" - dataset object (see above)

After running through the split_training_test function, the following keys are added: 

"x_train" - x vales for training set
"x_test" - x values for test set
"y_train" - y values for training set
"y_test" - y values for test set
"x_train_key" - x keys for training set
"x_test_key" - x keys for test set
"y_train_key" - y keys for training set 
"y_test_key" - y keys for test set 


### File naming schema 
The dataset will be located in the folder specificed, under a sub-folder corresponding to the model index, i.e. {subpath}/{model_index}
Input values are named {dataset_name}_x.npy
Output values are named {dataset_name}_y.npy
Input key values (usually the date) are named {dataset_name}_x_key.npy
Output key values (usually the date) are named {dataset_name}_y_key.npy
The dataset object is saved as a json file under {dataset_name}_dataset_object.json




