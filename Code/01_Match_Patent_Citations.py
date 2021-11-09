import pandas as pd
from time import time, sleep

"""""""""""""""""""""""""""

MICRON TECHNOLOGY

"""""""""""""""""""""""""""

file = pd.read_csv("Micron_Technology_Citations_raw.csv", sep=";", header=0, usecols=["Document", "Child", "Dur. [Parent PD -> Child PD]", "Assignee Name"]).dropna(how="all")
print(len(file))

document=[]
doc = int()
for index,row in file.iterrows():
    if str(row["Document"]) == "nan":
        document.append(doc)
    else:
        doc = int(row["Document"])
        document.append(doc)
file["Document"] = document

#only patents from Micron
different_writings_of_assignee = ["micron", "micron,", "micronbtechnology,", "microntechnology,", "microntechnology"]
Micron = []
for index, row in file.iterrows():
    assignee = row['Assignee Name']
    assignee = str(assignee).lower()
    assignee = assignee.split()
    if any(word in assignee for word in different_writings_of_assignee):
        Micron.append(1)
    else:
        Micron.append(0)        
file["Micron_assignee"] = Micron

df_filtered = file[:]

df_filtered = df_filtered.to_numpy()

citation = []
patent = []
assignee_patent = []
assignee_citation = []
time_gap = []
selfcitation = []
selfcitations = []
non_selfcitations = []
counter = 0
t1 = time()

len_matrix = len(df_filtered)

sleep(5)
for index in df_filtered:
    if ((counter+1) % 10000) ==0:
        print("\nNext 10000 rows processed in {0} seconds ({1} of {2}).".format(int(time()-t1), counter+1, len(df_filtered)))
        #sleep(2)
        t1 = time()
    counter += 1
    focal_patent = index[0]
    if str(index[1]) == "nan":
        assignee_name_patent = index[3]
        num_assignee = 1
        for i in assignee_name_patent:
            if i == "|":
                num_assignee += 1
    else:
        child = int(index[1])
        
        if index[4] == 1:
            selfcitation.append(1)
            selfcitations.append(child)
        else:
            selfcitation.append(0)
            non_selfcitations.append(child)
        
        patent.append(focal_patent)
        assignee_patent.append(assignee_name_patent)
        time_gap.append(round(index[2],2))
        
        citation.append(child)
        assignee_name_citation = index[3]
        assignee_citation.append(assignee_name_citation)

df = pd.DataFrame(data=zip(patent, assignee_patent, citation, selfcitation, assignee_citation, time_gap), columns = ["Focal_Patent", "Assignee_Focal_Patent", "Citation",  "Selfcitation", "Assignee_Citation", "Issue_to_File_in_Years"])
df.to_excel("Micron_Citations.xlsx", index=False)

"""""""""""""""""""""""""""

IBM

"""""""""""""""""""""""""""

file = pd.read_csv("IBM_Citations_raw.csv", sep=";", header=0, usecols=["Document", "Child", "Dur. [Parent PD -> Child PD]", "Assignee Name"]).dropna(how="all")
print(len(file))


document=[]
doc = int()
for index,row in file.iterrows():
    if str(row["Document"]) == "nan":
        document.append(doc)
    else:
        doc = int(row["Document"])
        document.append(doc)
file["Document"] = document

#only patents from ibm
different_writings_of_assignee = ["ibm", "international business", 
                                  "international machine", "internationial business", 
                                  "internatonal business", "machines corporation", 
                                "machine corporation", "international, business"]
ibm = []
for index, row in file.iterrows():
    assignee = row['Assignee Name']
    assignee = str(assignee).lower()
    if any(word in assignee for word in different_writings_of_assignee):
        ibm.append(1)
    else:
        ibm.append(0)        
file["ibm_assignee"] = ibm

df_filtered = file[:]
df_filtered = df_filtered.to_numpy()


citation = []
patent = []
assignee_patent = []
assignee_citation = []
time_gap = []
selfcitation = []
selfcitations = []
non_selfcitations = []
counter = 0
t1 = time()

len_matrix = len(df_filtered)

sleep(5)
for index in df_filtered:
    if ((counter+1) % 10000) ==0:
        print("\nNext 10000 rows processed in {0} seconds ({1} of {2}).".format(int(time()-t1), counter+1, len(df_filtered)))
        #sleep(2)
        t1 = time()
    counter += 1
    focal_patent  = index[0]
    if str(index[1]) == "nan":
        assignee_name_patent = index[3]
        num_assignee = 1
        for i in assignee_name_patent:
            if i == "|":
                num_assignee += 1
    else:
        child = int(index[1])
        
        if index[4] == 1:
            selfcitation.append(1)
            selfcitations.append(child)
        else:
            selfcitation.append(0)
            non_selfcitations.append(child)
        
        patent.append(focal_patent)
        assignee_patent.append(assignee_name_patent)
        time_gap.append(round(index[2],2))
        
        citation.append(child)
        assignee_name_citation = index[3]
        assignee_citation.append(assignee_name_citation)

df = pd.DataFrame(data=zip(patent, assignee_patent, citation, selfcitation, assignee_citation, time_gap), columns = ["Focal_Patent", "Assignee_Focal_Patent", "Citation",  "Selfcitation", "Assignee_Citation", "Issue_to_File_in_Years"])
df.to_excel("IBM_Citations.xlsx", index=False)


"""""""""""""""""""""""""""

SAMSUNG

"""""""""""""""""""""""""""

file = pd.read_csv("Samsung_Citations_raw.csv", sep=";", header=0, usecols=["Document", "Child", "Dur. [Parent PD -> Child PD]", "Assignee Name"]).dropna(how="all")
print(len(file))

document=[]
doc = int()
for index,row in file.iterrows():
    if str(row["Document"]) == "nan":
        document.append(doc)
    else:
        doc = int(row["Document"])
        document.append(doc)
file["Document"] = document

#only patents from Samsung
different_writings_of_assignee = ["samsung", "samsung,"]
Samsung = []
for index, row in file.iterrows():
    assignee = row['Assignee Name']
    assignee = str(assignee).lower()
    if any(word in assignee for word in different_writings_of_assignee):
        Samsung.append(1)
    else:
        Samsung.append(0)        
file["Samsung_assignee"] = Samsung

df_filtered = file[:]
df_filtered = df_filtered.to_numpy()


# 5 years
citation = []
patent = []
assignee_patent = []
assignee_citation = []
time_gap = []
selfcitation = []
selfcitations = []
non_selfcitations = []
counter = 0
t1 = time()

len_matrix = len(df_filtered)

sleep(5)
for index in df_filtered:
    if ((counter+1) % 10000) ==0:
        print("\nNext 10000 rows processed in {0} seconds ({1} of {2}).".format(int(time()-t1), counter+1, len(df_filtered)))
        #sleep(2)
        t1 = time()
    counter += 1
    focal_patent  = index[0]
    if str(index[1]) == "nan":
        assignee_name_patent = index[3]
        num_assignee = 1
        for i in assignee_name_patent:
            if i == "|":
                num_assignee += 1
    else:
        child = int(index[1])
        
        if index[4] == 1:
            selfcitation.append(1)
            selfcitations.append(child)
        else:
            selfcitation.append(0)
            non_selfcitations.append(child)
        
        patent.append(focal_patent)
        assignee_patent.append(assignee_name_patent)
        time_gap.append(round(index[2],2))
        
        
        citation.append(child)
        assignee_name_citation = index[3]
        num_assignee_cit = 1
        for i in assignee_name_citation:
            if i == "|":
                num_assignee_cit += 1
        assignee_citation.append(assignee_name_citation)

df = pd.DataFrame(data=zip(patent, assignee_patent, citation, selfcitation, assignee_citation, time_gap), columns = ["Focal_Patent", "Assignee_Focal_Patent", "Citation",  "Selfcitation", "Assignee_Citation", "Issue_to_File_in_Years"])
df.to_excel("Samsung_Citations.xlsx", index=False)

"""""""""""""""""""""""""""

TOSHIBA

"""""""""""""""""""""""""""


file = pd.read_csv("Toshiba_Citations_raw.csv", sep=";", header=0, usecols=["Document", "Child", "Dur. [Parent PD -> Child PD]", "Assignee Name"]).dropna(how="all")
print(len(file))

document=[]
doc = int()
for index,row in file.iterrows():
    if str(row["Document"]) == "nan":
        document.append(doc)
    else:
        doc = int(row["Document"])
        document.append(doc)
file["Document"] = document

#only patents from Toshiba
different_writings_of_assignee = ["toshiba", "toshiba,", "kabushiki"]
Toshiba = []
for index, row in file.iterrows():
    assignee = row['Assignee Name']
    assignee = str(assignee).lower()
    assignee = assignee.split()
    if any(word in assignee for word in different_writings_of_assignee):
        Toshiba.append(1)
    else:
        Toshiba.append(0)        
file["Toshiba_assignee"] = Toshiba

df_filtered = file[:]
df_filtered = df_filtered.to_numpy()

citation = []
patent = []
assignee_patent = []
assignee_citation = []
time_gap = []
selfcitation = []
selfcitations = []
non_selfcitations = []
counter = 0
t1 = time()

len_matrix = len(df_filtered)

sleep(5)
for index in df_filtered:
    if ((counter+1) % 10000) ==0:
        print("\nNext 10000 rows processed in {0} seconds ({1} of {2}).".format(int(time()-t1), counter+1, len(df_filtered)))
        #sleep(2)
        t1 = time()
    counter += 1
    focal_patent  = index[0]
    if str(index[1]) == "nan":
        assignee_name_patent = index[3]
        num_assignee = 1
        for i in assignee_name_patent:
            if i == "|":
                num_assignee += 1
    else:
        child = int(index[1])
        
        if index[4] == 1:
            selfcitation.append(1)
            selfcitations.append(child)
        else:
            selfcitation.append(0)
            non_selfcitations.append(child)
        
        patent.append(focal_patent)
        assignee_patent.append(assignee_name_patent)
        time_gap.append(round(index[2],2))
        
        
        citation.append(child)
        assignee_name_citation = index[3]
        assignee_citation.append(assignee_name_citation)

df = pd.DataFrame(data=zip(patent, assignee_patent, citation, selfcitation, assignee_citation, time_gap), columns = ["Focal_Patent", "Assignee_Focal_Patent", "Citation",  "Selfcitation", "Assignee_Citation", "Issue_to_File_in_Years"])
df.to_excel("Toshiba_Citations.xlsx", index=False)