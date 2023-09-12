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
phase_name = "20"
#prev_phase_base = "20"
phase_path_start = "generated_files/"

 letters = ['E', 'F', 'G', 'H', 'J', 'L', 'M', 'N', 'Q', 'S', 'T', 'U', 'V', 
 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']

#letters = ['J', 'L', 'M', 'N', 'Q', 'S', 'T', 'U', 'V', 
#'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD']

print(len(letters))
input_days = [30, 60]
output_days = [1, 7]
#Going to use 0.7 factor going forward, from now on.   
use_scaling_factor = "0.7"
deep_lstm = False
deep_ae = True
test = False
conv = False
transfer_learn = False

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor, test=test)

