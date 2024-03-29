
import pickle 
import dataset_generator
import model_generator
import graph_and_visualize 


def make_datasets(phase_path):
    pathname = phase_path + "phase1_dataset_descriptors.pickle"
    with open(pathname, "rb") as f:
        dataset_descriptors = pickle.load(f)

    start_index=0
    for index in range(start_index, len(dataset_descriptors)):
        dataset_generator.create_dataset_from_dataset_object(dataset_descriptors[index])
    print("Finished making datasets")  


def alert(message):
    exec_string = f'mpack -s "{message}" alert.txt marzeverett@gmail.com'
    os.system(exec_string)


def run_experiments(phase_path):
    dataset_base_path = "generated_files/datasets/"
    e_pathname = phase_path + "phase1_experiment_descriptors.pickle"
    d_pathname = phase_path + "phase1_dataset_descriptors.pickle"
    #Load in descriptors 
    with open(e_pathname, "rb") as f:
        experiment_descriptors = pickle.load(f)
    start_index = 0
    end = len(experiment_descriptors)
    #Actually run the experiments 
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
            # message = f"Error on experiment index {i} for reason {e}"
            # alert(message) 
    print("FINISHED!")
    #Figure this out later 
    # message = f"Finished! {end} Experiments"
    # alert(message)