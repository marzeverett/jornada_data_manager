import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json 
import slate_library



################################################################

#Phase 4!!
#Phase 4 takes off datastreams and then retrains them. It is similar 
# to phase 2-3, but with considerably more finagling of the 
#retrain process. 

#Same basic processes. Taking out some 
phase_name = "7"
prev_phase_base = "7"
phase_path_start = "generated_files/"
letters = ["E", "G", "H", "J", "S", "T", "U", "V", "W"]
#letters = ["T", "U", "V", "W"]


old_delete_stream = "rain"
transfer_learn = True
transfer_dict = {
    "prev_phase": "5",
    "transfer_on": "ds",
    "delete_stream": old_delete_stream,
    "part_train_letters": ["E", "H"],
}

#letters = ['E', 'G']
#letters = ['G']

input_days = [30, 60]
output_days = [1, 7]
#Decide on this going forward based on results of 3.  
use_scaling_factor = "0.7"
#incoporate phase into base dataset name and base name!!! 
test = False
#ae model is prev base name concat with scaling factor 
#ae prev name is prev dataset name 

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor, prev_phase_base=prev_phase_base, test=test, transfer_learn=transfer_learn, transfer_dict=transfer_dict)

#IMPORTANT: How to handle the issue of pretraining? 
