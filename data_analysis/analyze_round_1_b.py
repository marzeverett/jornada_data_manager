#Help from:
#https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas 

import os 
import pandas as pd
import matplotlib.pyplot as plt 

#LOOK INTO
#Group by Documentation
#https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.groupby.html 

# colnames=['TIME', 'X', 'Y', 'Z'] 
# user1 = pd.read_csv('dataset/1.csv', names=colnames, header=None)
#https://www.geeksforgeeks.org/how-to-plot-multiple-data-columns-in-a-dataframe/ 
cols = [
    "version",
    "location_scheme",
    "datastream_scheme",
    "l_combo",
    "ds_combo",
    "input_days",
    "output_days",
    "loss",
    "mse",
    "mape",
    "mae",
    "dataset_size",
    "training_time",
    "experiment_name",
    "dataset_name",
    "epochs"
]

data = pd.read_csv('main_metrics/phase_1_B.csv', names=cols)

#print(data.head())

#data.plot(x="output_days", y=["mse"], kind="scatter")
#data.groupby(["input_days", "output_days"]).plot(x="output_days", y=["mse"], kind="scatter")
#data.groupby("input_days")["output_days"].plot(x="output_days", y=["mse"], kind="scatter")


#Look up - you need to make sure you know exactly what's its doing
#https://www.geeksforgeeks.org/pandas-groupby-multiple-values-and-plotting-results/ 
#df = data.groupby(["input_days", "output_days"]).mean()["mse"]

#df = data.loc[data["datastream_scheme"].isin([0, 1])].groupby(["location_scheme"]).mean()
#df2 = data.loc[data["datastream_scheme"].isin([2, 3])].groupby(["location_scheme"]).mean()


new_data = data.loc[(data["datastream_scheme"] == 3) & (data["location_scheme"] == 3)]

mean = round(new_data["mse"].mean(), 5)
std = round(new_data["mse"].std(), 5)
print("Mean", mean)
print("Standard Deviation", std)


df = new_data.groupby(["output_days"]).mean()

#df.plot(y="mse")
df.plot(kind="bar", y="mse")
#df2.plot(kind="bar", y="mse")
plt.xticks(rotation=30)
#plt.show()
save_name = "performance_by_experiment_num_nodes"
save_folder = "jornada_regression_base"
save_folder_path = "/home/marz/Documents/vineyard/Written Papers/Dissertation/Notes and Such/"+save_folder+"/"
if not os.path.exists(save_folder_path):
    os.makedirs(save_folder_path)
save_path = save_folder_path+save_name+".png"

plt.show()
#plt.savefig(save_path)








# # plot the dataframe
# df.plot(x="Name", y=["Price", "User Rating"], kind="bar", figsize=(9, 8))
 
# # print bar graph
# mp.show()

# # importing packages
# import seaborn
 
# # load dataset and view
# data = seaborn.load_dataset('exercise')
# print(data)
 
# # multiple groupby (pulse, diet and time)
# df = data.groupby(['pulse', 'diet', 'time']).count()['kind']
# print(df)
 
# # plot the result
# df.plot()
# plt.xticks(rotation=30)
# plt.show()