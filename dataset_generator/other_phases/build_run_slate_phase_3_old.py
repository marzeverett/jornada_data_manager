import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json 
import slate_library





################################################################

#Phase 3!!
#Phase 3 takes out the temperature datastream in the data descriptor library, to be added later. 
phase_name = "3"
phase_path_start = "generated_files/"
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
input_days = [30, 60]
output_days = [1, 7]
use_scaling_factor = "0.7"
#incoporate phase into base dataset name and base name!!! 

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor)