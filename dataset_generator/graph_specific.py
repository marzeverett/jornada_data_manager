
import pickle
import os
import graph_and_visualize

#Part to change!"
model_name = ""
dataset_name = ""


dd, dr, ed, er = graph_and_visualize.load_everything(model_name, dataset_name)
graph_and_visualize.just_visualize(dd, dr, ed, er)

