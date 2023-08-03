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
phase_name = "13"
prev_phase_base = "13"
phase_path_start = "generated_files/"
#Don't build new datasets!!! 
#Might not have to use all of the letters here, I think. 
#letters = ["E", "G", "H", "J", "S", "T", "U", "V", "W"]
letters = ["E", "G", "H", "J", "S", "T", "U", "V", "W"]
letters = ["D"]

#letters = ['A', 'B']
print(len(letters))
input_days = [30, 60]
output_days = [1, 7]
#Going to use 0.7 factor going forward, from now on.   
use_scaling_factor = "0.7"
deep_lstm = False
deep_ae = False
test = True
predict_type = "frost"

delete_stream = "temp_hum"
transfer_learn = False
transfer_dict = {
    "prev_phase": "11",
    "transfer_on": "ds",
    "delete_stream": old_delete_stream,
    "part_train_letters": ["E", "H"],
}

#test = False
#incoporate phase into base dataset name and base name!!! 

#ae model is prev base name concat with scaling factor 
#ae prev name is prev dataset name 

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor, prev_phase_base=prev_phase_base, deep_lstm=deep_lstm, test=test, deep_ae=deep_ae, predict_type=predict_type, delete_stream=delete_stream)

