import pandas as pd
import numpy as np
import statistics

data = pd.read_csv("All_aggregated_inverse.csv", sep=";", decimal=",") 
x_variable = 'filing_year'

variables = ['incl_unigram_red_linkage', 'incl_unigram_compl_linkage', 'incl_bigram_red_linkage', 'incl_bigram_compl_linkage']
y_variable = variables[0]
y_variable_double = y_variable
years = list(set(list(data[x_variable])))

years = [i for i in range(2000, 2007+1)]
years_charts = ["'"+str(i)[2:] for i in years]

y_variable = "mean_cumulative_" + y_variable


Micron_annual_average_cumulative = []
IBM_annual_average_cumulative = []
Samsung_annual_average_cumulative = []
Toshiba_annual_average_cumulative = []


data1 = data[data['Micron']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        Micron_annual_average_cumulative.append(statistics.mean(annual_values))
    else:
        Micron_annual_average_cumulative.append(np.nan)

data1 = data[data['IBM']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        IBM_annual_average_cumulative.append(statistics.mean(annual_values))
    else:
        IBM_annual_average_cumulative.append(np.nan)
        
data1 = data[data['Samsung']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        Samsung_annual_average_cumulative.append(statistics.mean(annual_values))
    else:
        Samsung_annual_average_cumulative.append(np.nan)
        
data1 = data[data['Toshiba']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        Toshiba_annual_average_cumulative.append(statistics.mean(annual_values))
    else:
        Toshiba_annual_average_cumulative.append(np.nan)
        
y_variable = "mean_preclusive_" + y_variable_double

values = Micron_annual_average_cumulative + IBM_annual_average_cumulative + Samsung_annual_average_cumulative + Toshiba_annual_average_cumulative
min_cum = min(values)
max_cum = max(values)

#min-max scaling

Micron_annual_average_cumulative = [((i-min_cum)/(max_cum-min_cum)) for i in Micron_annual_average_cumulative]
IBM_annual_average_cumulative = [(i-min_cum)/(max_cum-min_cum) for i in IBM_annual_average_cumulative]
Samsung_annual_average_cumulative = [(i-min_cum)/(max_cum-min_cum) for i in Samsung_annual_average_cumulative]
Toshiba_annual_average_cumulative = [(i-min_cum)/(max_cum-min_cum) for i in Toshiba_annual_average_cumulative]

values = Micron_annual_average_cumulative + IBM_annual_average_cumulative + Samsung_annual_average_cumulative + Toshiba_annual_average_cumulative
min_cum = min(values)
max_cum = max(values)

#median and mean von values bestimmen
median_cum = np.median(values)
mean_cum = statistics.mean(values)


Micron_annual_average_preclusive = []
IBM_annual_average_preclusive = []
Samsung_annual_average_preclusive = []
Toshiba_annual_average_preclusive = []


data1 = data[data['Micron']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        Micron_annual_average_preclusive.append(statistics.mean(annual_values))
    else:
        Micron_annual_average_preclusive.append(np.nan)

data1 = data[data['IBM']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        IBM_annual_average_preclusive.append(statistics.mean(annual_values))
    else:
        IBM_annual_average_preclusive.append(np.nan)
        
data1 = data[data['Samsung']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        Samsung_annual_average_preclusive.append(statistics.mean(annual_values))
    else:
        Samsung_annual_average_preclusive.append(np.nan)
        
data1 = data[data['Toshiba']==1]
for year in years: 
    df = data1[data1[x_variable]==year]
    annual_values = list(df[y_variable])
    if len(annual_values) > 0:
        Toshiba_annual_average_preclusive.append(statistics.mean(annual_values))
    else:
        Toshiba_annual_average_preclusive.append(np.nan)


values = Micron_annual_average_preclusive + IBM_annual_average_preclusive + Samsung_annual_average_preclusive + Toshiba_annual_average_preclusive
min_precl = min(values)
max_precl = max(values)


#min-max scaling
Micron_annual_average_preclusive = [((i-min_precl)/(max_precl-min_precl)) for i in Micron_annual_average_preclusive]
IBM_annual_average_preclusive = [(i-min_precl)/(max_precl-min_precl) for i in IBM_annual_average_preclusive]
Samsung_annual_average_preclusive = [(i-min_precl)/(max_precl-min_precl) for i in Samsung_annual_average_preclusive]
Toshiba_annual_average_preclusive = [(i-min_precl)/(max_precl-min_precl) for i in Toshiba_annual_average_preclusive]

values = Micron_annual_average_preclusive + IBM_annual_average_preclusive + Samsung_annual_average_preclusive + Toshiba_annual_average_preclusive
min_precl = min(values)
max_precl = max(values)


median_precl = np.median(values)
mean_precl = statistics.mean(values)

"""
PLOTTING: https://stackoverflow.com/questions/14432557/matplotlib-scatter-plot-with-different-text-at-each-data-point
"""

#plotting : 

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
sns.set_palette("colorblind")
mpl.rcParams['font.size'] = 8
mpl.rcParams["font.family"] = "calibri"

#fig, axes = plt.subplots(2, 2, sharex = True, sharey=True, figsize=(6.4, 4))
cm = 1/2.54
fig, axes = plt.subplots(2, 2, sharex = True, sharey=True, figsize=(16*cm, 16*cm))


axes[0,0].set_title('Micron Technology')
axes[0,1].set_title('IBM')
axes[1,0].set_title('Samsung')
axes[1,1].set_title('Toshiba')


mpl.rcParams['font.size'] = 8
    
axes[0,0].hlines(y = mean_precl, xmin = -1, xmax = max_cum+10, linestyles="dashed", colors = "grey", label="average", linewidth = 0.5)
axes[0,0].vlines(x = mean_cum, ymin = -1, ymax = max_precl+10, linestyles="dashed", colors = "grey",  linewidth = 0.5)

axes[0,1].hlines(y = mean_precl, xmin = -1, xmax = max_cum+10, linestyles="dashed", colors = "grey", label="average", linewidth = 0.5)
axes[0,1].vlines(x = mean_cum, ymin = -1, ymax = max_precl+10, linestyles="dashed", colors = "grey",  linewidth = 0.5)

axes[1,0].hlines(y = mean_precl, xmin = -1, xmax = max_cum+10, linestyles="dashed", colors = "grey", label="average", linewidth = 0.5)
axes[1,0].vlines(x = mean_cum, ymin = -1, ymax = max_precl+10, linestyles="dashed", colors = "grey",  linewidth = 0.5)

axes[1,1].hlines(y = mean_precl, xmin = -1, xmax = max_cum+10, linestyles="dashed", colors = "grey", label="average", linewidth = 0.5)
axes[1,1].vlines(x = mean_cum, ymin = -1, ymax = max_precl+10, linestyles="dashed", colors = "grey",  linewidth = 0.5)


axes[0,0].set_ylim([-.1, max_precl*1.1])
axes[0,0].set_xlim([-.1, max_cum*1.1])

axes[0,1].set_ylim([-.1, max_precl*1.1])
axes[0,1].set_xlim([-.1, max_cum*1.1])

axes[1,0].set_ylim([-.1, max_precl*1.1])
axes[1,0].set_xlim([-.1, max_cum*1.1])

axes[1,1].set_ylim([-.1, max_precl*1.1])
axes[1,1].set_xlim([-.1, max_cum*1.1])

plt.locator_params(axis="x", nbins=6)

plt.locator_params(axis="y", nbins=6)

mpl.rcParams['font.size'] = 8

dot_size = 5
colors = ["blue", "red", "orange", "green"]

axes[0,0].scatter(x=Micron_annual_average_cumulative, y=Micron_annual_average_preclusive, s=dot_size, c=colors[0])
for i, txt in enumerate(years_charts):
    axes[0,0].annotate(txt, (Micron_annual_average_cumulative[i], Micron_annual_average_preclusive[i]))
    
axes[0,0].scatter(x=[-100], y=[-100], s=dot_size, c="black", label="annual average")

axes[0,1].scatter(x=IBM_annual_average_cumulative, y=IBM_annual_average_preclusive, s=dot_size, c=colors[1])
for i, txt in enumerate(years_charts):
    axes[0,1].annotate(txt, (IBM_annual_average_cumulative[i], IBM_annual_average_preclusive[i]))
    
axes[1,0].scatter(x=Samsung_annual_average_cumulative, y=Samsung_annual_average_preclusive, s=dot_size, c=colors[2])
for i, txt in enumerate(years_charts):
    axes[1,0].annotate(txt, (Samsung_annual_average_cumulative[i], Samsung_annual_average_preclusive[i]))
    
axes[1,1].scatter(x=Toshiba_annual_average_cumulative, y=Toshiba_annual_average_preclusive, s=dot_size, c=colors[3])
for i, txt in enumerate(years_charts):
    axes[1,1].annotate(txt, (Toshiba_annual_average_cumulative[i], Toshiba_annual_average_preclusive[i]))

mpl.rcParams['font.size'] = 10
axes[0,0].set_ylabel("Preclusive GA", fontstyle="italic")

axes[1,0].set_ylabel("Preclusive GA", fontstyle="italic")
axes[1,0].set_xlabel("Cumulative GA",fontstyle="italic")
axes[1,1].set_xlabel("Cumulative GA", fontstyle="italic")
mpl.rcParams['font.size'] = 8
axes[0,0].legend()
mpl.rcParams['font.size'] = 12
#fig.suptitle('Generative Appropriability by Year')

plt.tight_layout()
y_variable = y_variable_double
plt.savefig("Generative_Appropriability_Matrix_{0}.png".format(y_variable), dpi=1600)
plt.savefig("Generative_Appropriability_Matrix_{0}.eps".format(y_variable), dpi=1600, format="eps")
plt.plot()
