import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json 



def return_experiment_1():
    experiment_1 = {
    "model": {
        "kind": "LSTM",
        "model_type": "Sequential",
        "layers": 
            [
                {
                    "type": "LSTM",
                    "num_nodes": 32,
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
        "epochs": 10,
        "test_split": 0.1,
        "validation_split": 0.2,
        "use_multiprocessing": True,
        #"metrics": ["mse"]
        "metrics": ["mse"],
        "verbose": True,
    },
    "experiment_folder_path": "generated_files/experiments/",
    "experiment_name": "test_experiment_7"
    }
    return experiment_1


################################################################

#Phase 2!!
#Phase 2 is exactly the same as phase 1, except is uses a 0.7 AE scaling factor 
phase_name = "2"
phase_path_start = "generated_files/"
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
input_days = [30, 60]
output_days = [1, 7]
use_scaling_factor = "0.7"
#incoporate phase into base dataset name and base name!!! 

#ae model is prev base name concat with scaling factor 
#ae prev name is prev dataset name 


parameter_dict_list = []
for letter in letters:
    new_dict = {}
    new_dict["phase_metrics"] = phase_name+"_"+letter
    new_dict["phase_path"] = phase_path_start+phase_name+"_"+letter+"/"
    new_dict["input_days"] = input_days
    new_dict["output_days"] = output_days
    new_dict["base_dataset_name"] = phase_name+"_"+letter
    new_dict["base_name"] = phase_name+"_"+letter+"_exp"
    if letter == 'A':
        new_dict["target_model"] = "ae"
        new_dict["list_of_base_sets"] = [3,4]
        new_dict["scaling_factors"] = [0.3, 0.5, 0.7, 0.9]
    elif letter == 'B':
        prev_letter = "A"
        new_dict["target_model"] = "time_regression"
        new_dict["list_of_base_sets"] = [3, 4]
        new_dict["scaling_factors"] = [8, 32, 64]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
    elif letter == 'C':
        prev_letter = "A"
        new_dict["target_model"] = "ae"
        new_dict["list_of_base_sets"] = [1, 2]
        new_dict["scaling_factors"] = [0.3, 0.5, 0.7, 0.9]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
        new_dict["ae_synthesis"] = "ds"
    elif letter == 'D':
        prev_letter = "C"
        new_dict["target_model"] = "time_regression"
        new_dict["list_of_base_sets"] = [1,2]
        new_dict["scaling_factors"] = [8, 32, 64]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
    elif letter == 'E':
        new_dict["target_model"] = "ae"
        new_dict["list_of_base_sets"] = [1,2]
        new_dict["scaling_factors"] = [0.3, 0.5, 0.7, 0.9]
    elif letter == 'F':
        prev_letter = "E"
        new_dict["target_model"] = "time_regression"
        new_dict["list_of_base_sets"] = [1, 2]
        new_dict["scaling_factors"] = [8, 32, 64]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
    elif letter == 'G':
        new_dict["target_model"] = "ae"
        new_dict["list_of_base_sets"] = [2,3]
        new_dict["scaling_factors"] = [0.3, 0.5, 0.7, 0.9]
    elif letter == 'H':
        prev_letter = "G"
        new_dict["target_model"] = "time_regression"
        new_dict["list_of_base_sets"] = [2, 3]
        new_dict["scaling_factors"] = [8, 32, 64]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
    elif letter == 'I':
        prev_letter = "G"
        new_dict["target_model"] = "ae"
        new_dict["list_of_base_sets"] = [1, 4]
        new_dict["scaling_factors"] = [0.3, 0.5, 0.7, 0.9]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
        new_dict["ae_synthesis"] = "l"
    elif letter == 'J':
        prev_letter = "I"
        new_dict["target_model"] = "time_regression"
        new_dict["list_of_base_sets"] = [1, 4]
        new_dict["scaling_factors"] = [8, 32, 64]
        model_name = phase_name+"_"+prev_letter+"_exp"+str(use_scaling_factor)
        new_dict["ae_models"]= [model_name]
        prev_dataset_name = phase_name+"_"+prev_letter
        new_dict["ae_prev_names"]=  [prev_dataset_name]
    parameter_dict_list.append(new_dict)

print(json.dumps(parameter_dict_list, indent=4))


#RUN THEM HERE 
for parameters_dict in parameter_dict_list:
    print(f"Phase {phase_name} Letter: {parameters_dict['phase_metrics']}")
    #Generate descriptors 
    descriptors_list = ddl.run_generate(parameters_dict)
    print(descriptors_list[0])
    #Save the list 
    ddl.save_list(parameters_dict, descriptors_list)

    # # #The below for a quick test run. 
    # indexes = [0]
    # experiment_1 = return_experiment_1()
    # ddl.run_test(indexes, experiment_1, descriptors_list)

    #Make the datasets
    marl.make_datasets(parameters_dict["phase_path"])

    #Make the experiment descriptors
    experiments = edl.run_generate(parameters_dict)
    edl.save_list(parameters_dict, experiments)

    #Run the experiments 
    marl.run_experiments(parameters_dict["phase_path"])
    

