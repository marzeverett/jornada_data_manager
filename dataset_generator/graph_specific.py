
import pickle
import os
import graph_and_visualize

#Part to change!"
model_name = "3_T_exp64"
dataset_name = "3_T.v1.l0.ds0.l_combo0.ds_combo0.idays60.odays1"


dd, dr, ed, er = graph_and_visualize.load_everything(model_name, dataset_name)
graph_and_visualize.just_visualize(dd, dr, ed, er)

