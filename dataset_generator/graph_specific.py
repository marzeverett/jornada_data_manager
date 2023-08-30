
import pickle
import os
import graph_and_visualize

#Part to change!"
model_name = "8_AA_exp64"
dataset_name = "8_AA.v1.l0.ds1.l_combo0.ds_combo1.idays60.odays7"


path_start =f"/media/maryeverett/Backup4.0TB/Backup_8_16_23/jornada_data_manager/dataset_generator/"

dd, dr, ed, er = graph_and_visualize.load_everything(model_name, dataset_name, path_start=path_start)
graph_and_visualize.just_visualize(dd, dr, ed, er)

