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
phase_name = "5"
prev_phase_base = "5"
phase_path_start = "generated_files/"
#Don't build new datasets!!! 
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
'I', 'J', 'L', 'M', 'N', 'Q', 'S', 'T', 'U', 'V', 
'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 
'AF', 'AG', 'AH', 'AI', 'AJ']

delete_stream = "rain"

#letters = ['A', 'B']
print(len(letters))
input_days = [30, 60]
output_days = [1, 7]
#Decide on this going forward based on results of 3.  
use_scaling_factor = "0.7"
#incoporate phase into base dataset name and base name!!! 

#ae model is prev base name concat with scaling factor 
#ae prev name is prev dataset name 

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor, prev_phase_base=prev_phase_base, delete_stream=delete_stream)

