import pandas as pd
import copy

data_1 = pd.read_csv("All_inclusion_paired.csv" , sep=";", decimal=".")

data_2 = copy.deepcopy(data_1)
data_2['Assignee_Focal_Patent'] = ["All Firms" for i in range(data_2.shape[0])]

data = pd.DataFrame()
data = data.append(data_1)
data = data.append(data_2)

#t test and mann whitney u test
from scipy.stats import ttest_ind
import statistics

variants = list(data.columns)[6:10]
for variant in variants:
    with open("Knowledge flow per patent family membership tests_{0}.txt".format(variant), mode="w") as file:
        """
        T TEST for ALL FIRMS
        """
        file.write("ALL FIRMS")
        file.write("\n")
        file.write("\n")
        data2 = data[data['Assignee_Focal_Patent']=="All Firms"]
        same_family = list(data2[data2["same_family"]==1][variant])
        not_same_family = list(data2[data2["same_family"]==0][variant])
        ttest = ttest_ind(same_family, not_same_family, equal_var=False)
        mean_same_family = statistics.mean(same_family)
        mean_not_same_family = statistics.mean(not_same_family)
        sd_same_family = statistics.stdev(same_family)
        sd_not_same_family = statistics.stdev(not_same_family)
        
        file.write("T-test of independent means and unequal variances: {0}, t-statistic = {1}, p = {2}, Mean of same family = {3}, Mean of not same family = {4}.".format(str(ttest), str(ttest[0]), str(ttest[1]), str(mean_same_family), str(mean_not_same_family)))
        file.write("\n")
        file.write("\n")
        if mean_same_family > mean_not_same_family:
            file.write("The mean KNOWLEDGE FLOW between patents of the same family is significantly GREATER than the mean KNOWLEDGE FLOW between patents that do not belong to the same family.")
    
        """
        T TEST for Micron Technology
        """
        file.write("\n")
        file.write("\n")
        file.write("Micron Technology")
        file.write("\n")
        file.write("\n")
        data2 = data[data['Assignee_Focal_Patent']=="Micron Technology"]
        same_family = list(data2[data2["same_family"]==1][variant])
        not_same_family = list(data2[data2["same_family"]==0][variant])
        ttest = ttest_ind(same_family, not_same_family, equal_var=False)
        mean_same_family = statistics.mean(same_family)
        mean_not_same_family = statistics.mean(not_same_family)
        sd_same_family = statistics.stdev(same_family)
        sd_not_same_family = statistics.stdev(not_same_family)
        
        file.write("T-test of independent means and unequal variances: {0}, t-statistic = {1}, p = {2}, Mean of same family = {3}, Mean of not same family = {4}.".format(str(ttest), str(ttest[0]), str(ttest[1]), str(mean_same_family), str(mean_not_same_family)))
        file.write("\n")
        file.write("\n")
        if mean_same_family > mean_not_same_family:
            file.write("The mean KNOWLEDGE FLOW between patents of the same family is significantly GREATER than the mean KNOWLEDGE FLOW between patents that do not belong to the same family.")
    
        """
        T TEST for IBM
        """
        file.write("\n")
        file.write("\n")
        file.write("IBM")
        file.write("\n")
        file.write("\n")
        data2 = data[data['Assignee_Focal_Patent']=="IBM"]
        same_family = list(data2[data2["same_family"]==1][variant])
        not_same_family = list(data2[data2["same_family"]==0][variant])
        ttest = ttest_ind(same_family, not_same_family, equal_var=False)
        mean_same_family = statistics.mean(same_family)
        mean_not_same_family = statistics.mean(not_same_family)
        sd_same_family = statistics.stdev(same_family)
        sd_not_same_family = statistics.stdev(not_same_family)
        
        file.write("T-test of independent means and unequal variances: {0}, t-statistic = {1}, p = {2}, Mean of same family = {3}, Mean of not same family = {4}.".format(str(ttest), str(ttest[0]), str(ttest[1]), str(mean_same_family), str(mean_not_same_family)))
        file.write("\n")
        file.write("\n")
        if mean_same_family > mean_not_same_family:
            file.write("The mean KNOWLEDGE FLOW between patents of the same family is significantly GREATER than the mean KNOWLEDGE FLOW between patents that do not belong to the same family.")
    
        """
        T TEST for Samsung
        """
        file.write("\n")
        file.write("\n")
        file.write("Samsung")
        file.write("\n")
        file.write("\n")
        data2 = data[data['Assignee_Focal_Patent']=="Samsung"]
        same_family = list(data2[data2["same_family"]==1][variant])
        not_same_family = list(data2[data2["same_family"]==0][variant])
        ttest = ttest_ind(same_family, not_same_family, equal_var=False)
        mean_same_family = statistics.mean(same_family)
        mean_not_same_family = statistics.mean(not_same_family)
        sd_same_family = statistics.stdev(same_family)
        sd_not_same_family = statistics.stdev(not_same_family)
        
        file.write("T-test of independent means and unequal variances: {0}, t-statistic = {1}, p = {2}, Mean of same family = {3}, Mean of not same family = {4}.".format(str(ttest), str(ttest[0]), str(ttest[1]), str(mean_same_family), str(mean_not_same_family)))
        file.write("\n")
        file.write("\n")
        if mean_same_family > mean_not_same_family:
            file.write("The mean KNOWLEDGE FLOW between patents of the same family is significantly GREATER than the mean KNOWLEDGE FLOW between patents that do not belong to the same family.")
            
        """
        T TEST for Toshiba
        """
        file.write("\n")
        file.write("\n")
        file.write("Toshiba")
        file.write("\n")
        file.write("\n")
        data2 = data[data['Assignee_Focal_Patent']=="Toshiba"]
        same_family = list(data2[data2["same_family"]==1][variant])
        not_same_family = list(data2[data2["same_family"]==0][variant])
        ttest = ttest_ind(same_family, not_same_family, equal_var=False)
        mean_same_family = statistics.mean(same_family)
        mean_not_same_family = statistics.mean(not_same_family)
        sd_same_family = statistics.stdev(same_family)
        sd_not_same_family = statistics.stdev(not_same_family)
        
        file.write("T-test of independent means and unequal variances: {0}, t-statistic = {1}, p = {2}, Mean of same family = {3}, Mean of not same family = {4}.".format(str(ttest), str(ttest[0]), str(ttest[1]), str(mean_same_family), str(mean_not_same_family)))
        file.write("\n")
        file.write("\n")
        if mean_same_family > mean_not_same_family:
            file.write("The mean KNOWLEDGE FLOW between patents of the same family is significantly GREATER than the mean KNOWLEDGE FLOW between patents that do not belong to the same family.")
