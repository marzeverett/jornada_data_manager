import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json 
import slate_library



################################################################

#Phase 5!!
#Phase 5 takes off datastreams and then retrains them. It is similar 
# to phase 2-3, but with considerably more finagling of the 
#retrain process. 

#Phase 5 takes out rain 

#Same basic processes. Taking out some 
phase_name = "25"
prev_phase_base = "25"
phase_path_start = "generated_files/"
#Don't build new datasets!!! 
#Might not have to use all of the letters here, I think. 
letters = ["G", "J", "T", "V", "W"]

#letters = ['A', 'B']
print(len(letters))
input_days = [30, 60]
output_days = [1, 7]
#Going to use 0.7 factor going forward, from now on.   
use_scaling_factor = "0.7"
deep_lstm = False
deep_ae = False
test = False
predict_type = "frost"

old_delete_stream = "temp_hum"
transfer_learn = True
transfer_dict = {
    "prev_phase": "22",
    "transfer_on": "ds",
    "delete_stream": old_delete_stream,
    "part_train_letters": ["E", "H"],
}
prev_phase_base = "24"

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor, prev_phase_base=prev_phase_base, test=test, predict_type=predict_type, transfer_learn=transfer_learn, transfer_dict=transfer_dict)

