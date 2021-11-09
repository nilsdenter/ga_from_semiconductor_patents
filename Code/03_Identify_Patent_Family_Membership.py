import pandas as pd
from time import time

"""
Download the file "rel_app_text.tsv" from https://patentsview.org/download/data-download-tables
"""

rel_app_text = pd.read_csv("rel_app_text.tsv", sep="\t", index_col=1)
rel_app_text_index = set(rel_app_text.index)

patent_to_patent_table = pd.read_csv("All_inclusion_paired.csv", sep=";")
patents = list(patent_to_patent_table["Focal_Patent"]) + list(patent_to_patent_table["Citation"])
patents = set(patents)
patents = list(set([str(i) for i in patents]))

patent_families = {}
continuations = {}
divisionals = {}
provisionals = {}
t0 = time()
counter = 0
for number, patent in enumerate(patents):
    if patent in rel_app_text_index:
        text = rel_app_text.loc[patent,"text"]
        if str(text) == "nan": continue
        try:
            text.split()
        except:
            new_text = ""
            for item in range(len(text)):
                new_text += text[item]
                new_text += " "
            text = new_text
        text = text.replace(".","")
        text = text.replace(",", "")
        text = text.replace("/","")
        text = text.replace("-"," ")
        
        text = text.split()
        text = [word.lower() for word in text]
        #mode=0 no special mode, mode=1 continuation, mode=2, divisional, mode=3 provisional
        mode=0
        for word in text:
            if word == "continuation":
                mode=1
            if word == "divisional" or word == "division":
                mode=2
            if word == "provisional":
                mode=3
            if word.isdigit() and len(word)>=6:
                if patent in patent_families:
                    patent_families[patent] += [word]
                else: patent_families[patent] = [word]
                if mode == 1:
                    if patent in continuations:
                        continuations[patent] += [word]
                    else: continuations[patent] = [word]
                if mode == 2:
                    if patent in divisionals:
                        divisionals[patent] += [word]
                    else: divisionals[patent] = [word]                
                if mode == 3:
                    if patent in provisionals:
                        provisionals[patent] += [word]
                    else: provisionals[patent] = [word]                
        counter += 1
    if (number+1)%1000==0:
        print("Next 1000 patents processed in {2} seconds ({0} of {1})".format(number+1, len(patents), int(time()-t0)))
        
        
same_family_binary = []

for index, row in patent_to_patent_table.iterrows():
    if row["Selfcitation"] == 0:
        same_family_binary.append(0)
        continue
    index = str(row["Focal_Patent"])
    same_family = 0
    if index in patent_families:
        candidates_1 = set(patent_families[index])
    else: candidates_1 = set()
    
    citation = str(row["Citation"])
    if citation in patent_families:
        candidates_2 = set(patent_families[citation])
    else: candidates_2 = set()
    
    #patent is successor of citation
    for patent in candidates_1:
        if patent == citation and same_family == 0:
            same_family = 1
    #citation is successor of patent
    for patent in candidates_2:
        if patent == index and same_family == 0:
            same_family = 1
           
    #patent and citation share the same predecessor
    if len(candidates_1.intersection((candidates_2)))!=0:
        same_family = 1
    
    same_family_binary.append(same_family)
    
    
patent_to_patent_table["same_family"] = same_family_binary
print(sum(patent_to_patent_table[patent_to_patent_table["Selfcitation"]==0]["same_family"]))
print(sum(patent_to_patent_table[patent_to_patent_table["Selfcitation"]==1]["same_family"]))
patent_to_patent_table.to_csv("All_inclusion_paired.csv", sep=";", index=False)