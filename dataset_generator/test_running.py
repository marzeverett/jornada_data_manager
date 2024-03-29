import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 

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


parameters_dict = {
    "phase_path": "generated_files/phase_1_ae_individual/",
    "input_days": [30, 60],
    "output_days": [1, 7],
    "target_model": "time_regression",
    "base_dataset_name": "simple_reg_weather_ae",
    "list_of_base_sets": [3, 4],
    "ae_models": [],
    "ae_prev_names":  [],
    "base_name": "ae_individual",
    "scaling_factors": [8, 32, 64]
}



#Generate descriptors 
descriptors_list = ddl.run_generate(parameters_dict)
print(descriptors_list[0])
# #Save the list 
# ddl.save_list(parameters_dict, descriptors_list)

# #The below for a quick test run. 
indexes = [0]
experiment_1 = return_experiment_1()
ddl.run_test(indexes, experiment_1, descriptors_list)

# #Make the datasets
# marl.make_datasets(parameters_dict["phase_path"])

# #Make the experiment descriptors
# experiments = run_generate(parameters_dict)
# save_list(parameters_dict, experiments)

# #Run the experiments 
# marl.run_experiments(parameters_dict["phase_path"])
 

