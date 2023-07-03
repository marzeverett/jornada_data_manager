import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json 
import slate_library



################################################################

#Phase 3!!
#Phase 3 is exactly the same as phase 2, except is uses a 0.7 AE scaling factor 
#It is reusing the same 
phase_name = "3"
prev_phase_base = "2"
phase_path_start = "generated_files/"
#Don't build new datasets!!! 
# letters = ["F","G", "I", "J", "M", "N", "Q", "T", "V", "W", "Y",
#  "AA", "AB", "AD", "AF", "AG", "AI", "AJ"]

letters = ["I", "J", "M", "N", "Q", "T", "V", "W", "Y",
 "AA", "AB", "AD", "AF", "AG", "AI", "AJ"]

#letters = ['A', 'B']
print(len(letters))
input_days = [30, 60]
output_days = [1, 7]
use_scaling_factor = "0.7"
#incoporate phase into base dataset name and base name!!! 

#ae model is prev base name concat with scaling factor 
#ae prev name is prev dataset name 

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor, prev_phase_base=prev_phase_base)

