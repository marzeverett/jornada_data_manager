
import pickle
import os
import graph_and_visualize

#Part to change!"
model_name = "2_AF_exp32"
dataset_name = "2_AF.v1.l1.ds0.l_combo6.ds_combo0.idays30.odays1"


dd, dr, ed, er = graph_and_visualize.load_everything(model_name, dataset_name)
graph_and_visualize.just_visualize(dd, dr, ed, er)

