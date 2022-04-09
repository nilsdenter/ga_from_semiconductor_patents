import pandas as pd
import copy

x_variable = 'Patent_Filing_to_Citation_Filing' 
data_1 = pd.read_csv("All_inclusion_paired.csv" , sep=";", decimal=".")

data_2 = copy.deepcopy(data_1)
data_2['Assignee_Focal_Patent'] = ["All Firms" for i in range(data_2.shape[0])]

data = pd.DataFrame()
data = data.append(data_1)
data = data.append(data_2)

sf = []

for index, row in data.iterrows():
    if row["same_family"] == 1: sf.append("Yes")
    else: sf.append("No")
data["same_family"] = sf
data.rename(columns={"same_family": "Same Family"})

data = data[(data[x_variable] >=0) & (data[x_variable] <=20)]

variables = ['Inclusion Reduced Linkage Unigrams', 'Inclusion Complete Linkage Unigrams', 'Inclusion Reduced Linkage Bigrams', 'Inclusion Complete Linkage Bigrams']

y_variable = variables[0]

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set_palette(['#000000'], n_colors=100)

mpl.rcParams["font.family"] = "calibri"
cm = 1/2.54
fig, axes = plt.subplots(figsize=(14*cm, 8*cm))

sns.lineplot(ax = axes, data=data, x=x_variable, y=y_variable, style='Assignee_Focal_Patent')

mpl.rcParams['font.size'] = 12
#axes.set_title('Knowledge Flow by Time Lag')
mpl.rcParams['font.size'] = 8
axes.set_xticks([0, 5, 10, 15, 20])
axes.grid()

mpl.rcParams['font.size'] = 10
axes.set_xlabel("Time Lag in Years", fontstyle = "italic") 
axes.set_ylabel("Knowledge Flow", fontstyle = "italic")

mpl.rcParams['font.size'] = 8
handles, labels = axes.get_legend_handles_labels()
labels[0] = "Micron Technology"

handles_new, labels_new = handles[:], labels[:]

handles_new[1], labels_new[1] = handles[3], labels[3]
handles_new[2], labels_new[2] = handles[1], labels[1]
handles_new[3], labels_new[3] = handles[2], labels[2]



plt.legend(handles_new, labels_new, title=None)
plt.tight_layout()

plt.savefig("{0}_Knowledge_flow_by_time_lag_by_firm.png".format(y_variable), dpi=1600)
plt.savefig("{0}_Knowledge_flow_by_time_lag_by_firm.svg".format(y_variable), dpi=1600, format="svg")
plt.plot()

#average 0 years
import statistics

for i in range(0,20):
    data2 = data[data[x_variable]==i]
    print("The average at {0} years is a knowledge flow of {1}".format(i, statistics.mean(data2[y_variable])))

