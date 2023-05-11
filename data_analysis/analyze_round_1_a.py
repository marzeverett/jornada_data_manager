#Help from:
#https://stackoverflow.com/questions/31645466/give-column-name-when-read-csv-file-pandas 

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
    "dataset_size",
    "training_time",
    "experiment_name",
    "dataset_name"
]

data = pd.read_csv('1_main_metrics.csv', names=cols)

print(data.head())

#data.plot(x="output_days", y=["mse"], kind="scatter")
#data.groupby(["input_days", "output_days"]).plot(x="output_days", y=["mse"], kind="scatter")
#data.groupby("input_days")["output_days"].plot(x="output_days", y=["mse"], kind="scatter")


#Look up - you need to make sure you know exactly what's its doing
#https://www.geeksforgeeks.org/pandas-groupby-multiple-values-and-plotting-results/ 
#df = data.groupby(["input_days", "output_days"]).mean()["mse"]

df = data.groupby(["input_days", "output_days"]).mean()
#df = data.groupby(["input_days", "output_days"])

#df.plot(y="mse")
df.plot(kind="bar", y="mse")
plt.xticks(rotation=30)
plt.show()

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