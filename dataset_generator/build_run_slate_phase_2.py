import data_descriptor_library as ddl 
import experiment_descriptor_library as edl 
import make_and_run_library as marl 
import json 
import slate_library



################################################################

#Phase 2!!
#Phase 2 is exactly the same as phase 1, except is uses a 0.7 AE scaling factor 
phase_name = "2"
phase_path_start = "generated_files/"
# letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
# 'I', 'J', 'L', 'M', 'N', 'Q', 'S', 'T', 'U', 'V', 
# 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 
# 'AF', 'AG', 'AH', 'AI', 'AJ']
# letters = ['H', 
# 'I', 'J', 'L', 'M', 'N', 'Q', 'S', 'T', 'U', 'V', 
# 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 
# 'AF', 'AG', 'AH', 'AI', 'AJ']

# letters = ['M', 'N', 'Q', 'S', 'T', 'U', 'V', 
# 'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 
# 'AF', 'AG', 'AH', 'AI', 'AJ']

letters = ['T', 'U', 'V', 
'W', 'X', 'Y', 'Z', 'AA', 'AB', 'AC', 'AD', 'AE', 
'AF', 'AG', 'AH', 'AI', 'AJ']
#letters = ['A', 'B']
print(len(letters))
input_days = [30, 60]
output_days = [1, 7]
use_scaling_factor = "0.5"
#incoporate phase into base dataset name and base name!!! 

#ae model is prev base name concat with scaling factor 
#ae prev name is prev dataset name 

slate_library.run(phase_name, phase_path_start, letters, input_days, output_days, use_scaling_factor)

