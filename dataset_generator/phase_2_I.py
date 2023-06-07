import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json

def return_experiment_1():
    experiment_1 = {
    "model": {
        "kind": "AE",
        "model_type": "Sequential",
        "layers": 
            [
                {
                    "type": "Dense",
                    "num_nodes": 10,
                    "activation": "relu",
                    "name": "latent_space"
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
# parameters_dict = {
#     "phase_path": "generated_files/phase_1_a_ae/",
#     "input_days": [30, 60],
#     "output_days": [1, 7],
#     "target_model": "ae",
#     "base_dataset_name": "reg_A",
#     "list_of_base_sets": [3, 4],
#     #"ae_models": ["ae_individual0.5"],
#     #"ae_prev_names":  ["simple_reg_weather_ae"],
#     "base_name": "AE_A",
#     "scaling_factors": [0.3, 0.5, 0.7, 0.9]
# }

#C for later -- won't work quite the same way. Will need some build intution 
#C: 
parameters_dict = {
    "phase_path": "generated_files/phase_1_i_ae/",
    "input_days": [30, 60],
    "output_days": [1, 7],
    "target_model": "ae",
    "base_dataset_name": "reg_I",
    "list_of_base_sets": [1, 4],
    "ae_models": ["AE_G0.5"],
    "ae_prev_names":  ["reg_G"],
    "ae_synthesis": "ds", #means you are synthesizing previous aes on this datastream 
    "base_name": "lstm_I",
    "scaling_factors": [0.3, 0.5, 0.7, 0.9]
}
#

#Generate descriptors 
descriptors_list = ddl.run_generate(parameters_dict)
print(json.dumps(descriptors_list[0], indent=4))
# #Save the list 
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
 



# ##
# ds = "ONE" 
# ds_combo_dict = return_input_output_dict_combo(ds, "ds")
# for l_combo_index in range(0, len(l_combo_dict["input"])):
#     for ds_combo_index in range(0, len(ds_combo_dict["input"])):