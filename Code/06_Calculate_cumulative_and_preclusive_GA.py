import pandas as pd
from time import time
t0 = time()
from statistics import mean
import copy


data = pd.read_csv("All_inclusion_paired.csv",sep=";", decimal=".")

citation_data = copy.deepcopy(data)

preclusive = citation_data.loc[citation_data["Selfcitation"] == 0]

min_prec_unigram_red_linkage = min([i for i in preclusive['Inclusion Reduced Linkage Unigrams'] if i !=0])
min_prec_unigram_compl_linkage = min([i for i in preclusive['Inclusion Complete Linkage Unigrams'] if i !=0])
min_prec_bigram_red_linkage = min([i for i in preclusive['Inclusion Reduced Linkage Bigrams'] if i !=0])
min_prec_bigram_compl_linkage = min([i for i in preclusive['Inclusion Complete Linkage Bigrams'] if i !=0])

promote_prec_unigram_red_linkage = round(1/min_prec_unigram_red_linkage)
promote_prec_unigram_compl_linkage = round(1/min_prec_unigram_compl_linkage)
promote_prec_bigram_red_linkage = round(1/min_prec_bigram_red_linkage)
promote_prec_bigram_compl_linkage = round(1/min_prec_bigram_compl_linkage)

# =============================================================================
# promote_prec_unigram_red_linkage = 1000
# promote_prec_unigram_compl_linkage = 1000
# promote_prec_bigram_red_linkage = 1000
# promote_prec_bigram_compl_linkage = 1000
# =============================================================================

patent_id = []

mean_cumulative_incl_unigram_red_linkage = []
mean_cumulative_incl_unigram_compl_linkage = []
mean_cumulative_incl_bigram_red_linkage = []
mean_cumulative_incl_bigram_compl_linkage = []

mean_preclusive_incl_unigram_red_linkage = []
mean_preclusive_incl_unigram_compl_linkage = []
mean_preclusive_incl_bigram_red_linkage = []
mean_preclusive_incl_bigram_compl_linkage = []

assignee_name = []
micron = []
ibm = []
toshiba = []
samsung = []


filing_year = []
grant_year = []

"""""""""""""""""""""""""""

MICRON TECHNOLOGY

"""""""""""""""""""""""""""


citation_data = copy.deepcopy(data)
citation_data = citation_data[citation_data["Micron"]==1]

focal_patents = list(set(list(citation_data["Focal_Patent"])))
focal_patents.sort()
for patent in focal_patents:
    indexes = list(citation_data[citation_data["Focal_Patent"]== patent].index)
    patent_id.append(patent)
    
    cumulative_incl_unigram_red_linkage = []
    cumulative_incl_unigram_compl_linkage = []
    cumulative_incl_bigram_red_linkage = []
    cumulative_incl_bigram_compl_linkage = []
    
    preclusive_incl_unigram_red_linkage = []
    preclusive_incl_unigram_compl_linkage = []
    preclusive_incl_bigram_red_linkage = []
    preclusive_incl_bigram_compl_linkage = []
       
    self_cit = 0
    nonself_cit = 0
    
    for counter, index in enumerate(indexes):
        row = citation_data.loc[index,:]
        if counter == 0:            
            filing_year.append(row["Appl Year Focal Patent"])
            grant_year.append(row["Grant Year Focal Patent"])
            
            ibm.append(row["IBM"])
            micron.append(row["Micron"])
            samsung.append(row["Samsung"])
            toshiba.append(row["Toshiba"])
            assignee_name.append(row["Assignee_Focal_Patent"])
            
            counter = 1
        
        if row["Selfcitation"] == 1:
            cumulative_incl_unigram_red_linkage.append(row["Inclusion Reduced Linkage Unigrams"])
            cumulative_incl_unigram_compl_linkage.append(row["Inclusion Complete Linkage Unigrams"])
            cumulative_incl_bigram_red_linkage.append(row["Inclusion Reduced Linkage Bigrams"])
            cumulative_incl_bigram_compl_linkage.append(row["Inclusion Complete Linkage Bigrams"])
        
            self_cit += 1
           
        elif row["Selfcitation"] == 0:
            if row["Inclusion Reduced Linkage Unigrams"] != 0:
                preclusive_incl_unigram_red_linkage.append(1/row["Inclusion Reduced Linkage Unigrams"])
            else: preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
            
            if row["Inclusion Complete Linkage Unigrams"] != 0:  
                preclusive_incl_unigram_compl_linkage.append(1/row["Inclusion Complete Linkage Unigrams"])
            else: preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
            
            if row["Inclusion Reduced Linkage Bigrams"] != 0:         
                preclusive_incl_bigram_red_linkage.append(1/row["Inclusion Reduced Linkage Bigrams"])
            else: preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
            
            if row["Inclusion Complete Linkage Bigrams"] !=0:
                preclusive_incl_bigram_compl_linkage.append(1/row["Inclusion Complete Linkage Bigrams"])
            else: preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)

            nonself_cit += 1
    
    if len(cumulative_incl_unigram_red_linkage) == 0:
        mean_cumulative_incl_unigram_red_linkage.append(0)
        mean_cumulative_incl_unigram_compl_linkage.append(0)
        mean_cumulative_incl_bigram_red_linkage.append(0)
        mean_cumulative_incl_bigram_compl_linkage.append(0)
    else:
        mean_cumulative_incl_unigram_red_linkage.append(mean(cumulative_incl_unigram_red_linkage))
        mean_cumulative_incl_unigram_compl_linkage.append(mean(cumulative_incl_unigram_compl_linkage))
        mean_cumulative_incl_bigram_red_linkage.append(mean(cumulative_incl_bigram_red_linkage))
        mean_cumulative_incl_bigram_compl_linkage.append(mean(cumulative_incl_bigram_compl_linkage))   

    if len(preclusive_incl_unigram_red_linkage) == 0:
        mean_preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
        mean_preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
        mean_preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
        mean_preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
        
    else:
        mean_preclusive_incl_unigram_red_linkage.append(mean(preclusive_incl_unigram_red_linkage))
        mean_preclusive_incl_unigram_compl_linkage.append(mean(preclusive_incl_unigram_compl_linkage))
        mean_preclusive_incl_bigram_red_linkage.append(mean(preclusive_incl_bigram_red_linkage))
        mean_preclusive_incl_bigram_compl_linkage.append(mean(preclusive_incl_bigram_compl_linkage))   

citation_data = copy.deepcopy(data)

"""""""""""""""""""""""""""

IBM

"""""""""""""""""""""""""""

citation_data = citation_data[citation_data["IBM"]==1]

focal_patents = list(set(list(citation_data["Focal_Patent"])))
focal_patents.sort()
for patent in focal_patents:
    indexes = list(citation_data[citation_data["Focal_Patent"]== patent].index)
    patent_id.append(patent)
    
    cumulative_incl_unigram_red_linkage = []
    cumulative_incl_unigram_compl_linkage = []
    cumulative_incl_bigram_red_linkage = []
    cumulative_incl_bigram_compl_linkage = []
    
    preclusive_incl_unigram_red_linkage = []
    preclusive_incl_unigram_compl_linkage = []
    preclusive_incl_bigram_red_linkage = []
    preclusive_incl_bigram_compl_linkage = []
    
    num_unique_unigrams_in_selfciting = []
    num_unigrams_in_selfciting = []
    num_unique_bigrams_in_selfciting = []
    num_bigrams_in_selfciting = []

    num_unique_unigrams_in_otherciting = []
    num_unigrams_in_otherciting = []
    num_unique_bigrams_in_otherciting = []
    num_bigrams_in_otherciting = []
    
    self_cit = 0
    nonself_cit = 0
    
    for counter, index in enumerate(indexes):
        row = citation_data.loc[index,:]
        if counter == 0:
            
            filing_year.append(row["Appl Year Focal Patent"])
            grant_year.append(row["Grant Year Focal Patent"])

            ibm.append(row["IBM"])
            micron.append(row["Micron"])
            samsung.append(row["Samsung"])
            toshiba.append(row["Toshiba"])
            assignee_name.append(row["Assignee_Focal_Patent"])
            
            counter = 1
        
        if row["Selfcitation"] == 1:
            cumulative_incl_unigram_red_linkage.append(row["Inclusion Reduced Linkage Unigrams"])
            cumulative_incl_unigram_compl_linkage.append(row["Inclusion Complete Linkage Unigrams"])
            cumulative_incl_bigram_red_linkage.append(row["Inclusion Reduced Linkage Bigrams"])
            cumulative_incl_bigram_compl_linkage.append(row["Inclusion Complete Linkage Bigrams"])
            
            num_unique_unigrams_in_selfciting.append(row["num_unique_unigrams_in_citation"])
            num_unigrams_in_selfciting.append(row["num_unigrams_in_citation"])
            num_unique_bigrams_in_selfciting.append(row["num_unique_bigrams_in_citation"])
            num_bigrams_in_selfciting.append(row["num_bigrams_in_citation"])  
        
            self_cit += 1
           
        elif row["Selfcitation"] == 0:
            if row["Inclusion Reduced Linkage Unigrams"] != 0:
                preclusive_incl_unigram_red_linkage.append(1/row["Inclusion Reduced Linkage Unigrams"])
            else: preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
            
            if row["Inclusion Complete Linkage Unigrams"] != 0:  
                preclusive_incl_unigram_compl_linkage.append(1/row["Inclusion Complete Linkage Unigrams"])
            else: preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
            
            if row["Inclusion Reduced Linkage Bigrams"] != 0:         
                preclusive_incl_bigram_red_linkage.append(1/row["Inclusion Reduced Linkage Bigrams"])
            else: preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
            
            if row["Inclusion Complete Linkage Bigrams"] !=0:
                preclusive_incl_bigram_compl_linkage.append(1/row["Inclusion Complete Linkage Bigrams"])
            else: preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
            
            num_unique_unigrams_in_otherciting.append(row["num_unique_unigrams_in_citation"])
            num_unigrams_in_otherciting.append(row["num_unigrams_in_citation"])
            num_unique_bigrams_in_otherciting.append(row["num_unique_bigrams_in_citation"])
            num_bigrams_in_otherciting.append(row["num_bigrams_in_citation"])    
            nonself_cit += 1
    
    if len(cumulative_incl_unigram_red_linkage) == 0:
        mean_cumulative_incl_unigram_red_linkage.append(0)
        mean_cumulative_incl_unigram_compl_linkage.append(0)
        mean_cumulative_incl_bigram_red_linkage.append(0)
        mean_cumulative_incl_bigram_compl_linkage.append(0)
    else:
        mean_cumulative_incl_unigram_red_linkage.append(mean(cumulative_incl_unigram_red_linkage))
        mean_cumulative_incl_unigram_compl_linkage.append(mean(cumulative_incl_unigram_compl_linkage))
        mean_cumulative_incl_bigram_red_linkage.append(mean(cumulative_incl_bigram_red_linkage))
        mean_cumulative_incl_bigram_compl_linkage.append(mean(cumulative_incl_bigram_compl_linkage))   

    if len(preclusive_incl_unigram_red_linkage) == 0:
        mean_preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
        mean_preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
        mean_preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
        mean_preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
        
    else:
        mean_preclusive_incl_unigram_red_linkage.append(mean(preclusive_incl_unigram_red_linkage))
        mean_preclusive_incl_unigram_compl_linkage.append(mean(preclusive_incl_unigram_compl_linkage))
        mean_preclusive_incl_bigram_red_linkage.append(mean(preclusive_incl_bigram_red_linkage))
        mean_preclusive_incl_bigram_compl_linkage.append(mean(preclusive_incl_bigram_compl_linkage))   

citation_data = copy.deepcopy(data)

"""""""""""""""""""""""""""

SAMSUNG

"""""""""""""""""""""""""""

citation_data = citation_data[citation_data["Samsung"]==1]

focal_patents = list(set(list(citation_data["Focal_Patent"])))
focal_patents.sort()
for patent in focal_patents:
    indexes = list(citation_data[citation_data["Focal_Patent"]== patent].index)
    patent_id.append(patent)
    
    cumulative_incl_unigram_red_linkage = []
    cumulative_incl_unigram_compl_linkage = []
    cumulative_incl_bigram_red_linkage = []
    cumulative_incl_bigram_compl_linkage = []
    
    preclusive_incl_unigram_red_linkage = []
    preclusive_incl_unigram_compl_linkage = []
    preclusive_incl_bigram_red_linkage = []
    preclusive_incl_bigram_compl_linkage = []
    
    num_unique_unigrams_in_selfciting = []
    num_unigrams_in_selfciting = []
    num_unique_bigrams_in_selfciting = []
    num_bigrams_in_selfciting = []

    num_unique_unigrams_in_otherciting = []
    num_unigrams_in_otherciting = []
    num_unique_bigrams_in_otherciting = []
    num_bigrams_in_otherciting = []
    
    self_cit = 0
    nonself_cit = 0
    
    for counter, index in enumerate(indexes):
        row = citation_data.loc[index,:]
        if counter == 0:
            
            filing_year.append(row["Appl Year Focal Patent"])
            grant_year.append(row["Grant Year Focal Patent"])
            
            ibm.append(row["IBM"])
            micron.append(row["Micron"])
            samsung.append(row["Samsung"])
            toshiba.append(row["Toshiba"])
            assignee_name.append(row["Assignee_Focal_Patent"])
            
            counter = 1
        
        if row["Selfcitation"] == 1:
            cumulative_incl_unigram_red_linkage.append(row["Inclusion Reduced Linkage Unigrams"])
            cumulative_incl_unigram_compl_linkage.append(row["Inclusion Complete Linkage Unigrams"])
            cumulative_incl_bigram_red_linkage.append(row["Inclusion Reduced Linkage Bigrams"])
            cumulative_incl_bigram_compl_linkage.append(row["Inclusion Complete Linkage Bigrams"])
            
            num_unique_unigrams_in_selfciting.append(row["num_unique_unigrams_in_citation"])
            num_unigrams_in_selfciting.append(row["num_unigrams_in_citation"])
            num_unique_bigrams_in_selfciting.append(row["num_unique_bigrams_in_citation"])
            num_bigrams_in_selfciting.append(row["num_bigrams_in_citation"])  
        
            self_cit += 1
           
        elif row["Selfcitation"] == 0:
            if row["Inclusion Reduced Linkage Unigrams"] != 0:
                preclusive_incl_unigram_red_linkage.append(1/row["Inclusion Reduced Linkage Unigrams"])
            else: preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
            
            if row["Inclusion Complete Linkage Unigrams"] != 0:  
                preclusive_incl_unigram_compl_linkage.append(1/row["Inclusion Complete Linkage Unigrams"])
            else: preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
            
            if row["Inclusion Reduced Linkage Bigrams"] != 0:         
                preclusive_incl_bigram_red_linkage.append(1/row["Inclusion Reduced Linkage Bigrams"])
            else: preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
            
            if row["Inclusion Complete Linkage Bigrams"] !=0:
                preclusive_incl_bigram_compl_linkage.append(1/row["Inclusion Complete Linkage Bigrams"])
            else: preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
            
            num_unique_unigrams_in_otherciting.append(row["num_unique_unigrams_in_citation"])
            num_unigrams_in_otherciting.append(row["num_unigrams_in_citation"])
            num_unique_bigrams_in_otherciting.append(row["num_unique_bigrams_in_citation"])
            num_bigrams_in_otherciting.append(row["num_bigrams_in_citation"])    
            nonself_cit += 1
    
    if len(cumulative_incl_unigram_red_linkage) == 0:
        mean_cumulative_incl_unigram_red_linkage.append(0)
        mean_cumulative_incl_unigram_compl_linkage.append(0)
        mean_cumulative_incl_bigram_red_linkage.append(0)
        mean_cumulative_incl_bigram_compl_linkage.append(0)
    else:
        mean_cumulative_incl_unigram_red_linkage.append(mean(cumulative_incl_unigram_red_linkage))
        mean_cumulative_incl_unigram_compl_linkage.append(mean(cumulative_incl_unigram_compl_linkage))
        mean_cumulative_incl_bigram_red_linkage.append(mean(cumulative_incl_bigram_red_linkage))
        mean_cumulative_incl_bigram_compl_linkage.append(mean(cumulative_incl_bigram_compl_linkage))   

    if len(preclusive_incl_unigram_red_linkage) == 0:
        mean_preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
        mean_preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
        mean_preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
        mean_preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
        
    else:
        mean_preclusive_incl_unigram_red_linkage.append(mean(preclusive_incl_unigram_red_linkage))
        mean_preclusive_incl_unigram_compl_linkage.append(mean(preclusive_incl_unigram_compl_linkage))
        mean_preclusive_incl_bigram_red_linkage.append(mean(preclusive_incl_bigram_red_linkage))
        mean_preclusive_incl_bigram_compl_linkage.append(mean(preclusive_incl_bigram_compl_linkage))   

citation_data = copy.deepcopy(data)

"""""""""""""""""""""""""""

TOSHIBA

"""""""""""""""""""""""""""

citation_data = citation_data[citation_data["Toshiba"]==1]

focal_patents = list(set(list(citation_data["Focal_Patent"])))
focal_patents.sort()
for patent in focal_patents:
    indexes = list(citation_data[citation_data["Focal_Patent"]== patent].index)
    patent_id.append(patent)
    
    cumulative_incl_unigram_red_linkage = []
    cumulative_incl_unigram_compl_linkage = []
    cumulative_incl_bigram_red_linkage = []
    cumulative_incl_bigram_compl_linkage = []
    
    preclusive_incl_unigram_red_linkage = []
    preclusive_incl_unigram_compl_linkage = []
    preclusive_incl_bigram_red_linkage = []
    preclusive_incl_bigram_compl_linkage = []
    
    num_unique_unigrams_in_selfciting = []
    num_unigrams_in_selfciting = []
    num_unique_bigrams_in_selfciting = []
    num_bigrams_in_selfciting = []

    num_unique_unigrams_in_otherciting = []
    num_unigrams_in_otherciting = []
    num_unique_bigrams_in_otherciting = []
    num_bigrams_in_otherciting = []
    
    self_cit = 0
    nonself_cit = 0
    
    for counter, index in enumerate(indexes):
        row = citation_data.loc[index,:]
        if counter == 0:
 
            filing_year.append(row["Appl Year Focal Patent"])
            grant_year.append(row["Grant Year Focal Patent"])
            
            ibm.append(row["IBM"])
            micron.append(row["Micron"])
            samsung.append(row["Samsung"])
            toshiba.append(row["Toshiba"])
            assignee_name.append(row["Assignee_Focal_Patent"])
            
            counter = 1
        
        if row["Selfcitation"] == 1:
            cumulative_incl_unigram_red_linkage.append(row["Inclusion Reduced Linkage Unigrams"])
            cumulative_incl_unigram_compl_linkage.append(row["Inclusion Complete Linkage Unigrams"])
            cumulative_incl_bigram_red_linkage.append(row["Inclusion Reduced Linkage Bigrams"])
            cumulative_incl_bigram_compl_linkage.append(row["Inclusion Complete Linkage Bigrams"])
            
            num_unique_unigrams_in_selfciting.append(row["num_unique_unigrams_in_citation"])
            num_unigrams_in_selfciting.append(row["num_unigrams_in_citation"])
            num_unique_bigrams_in_selfciting.append(row["num_unique_bigrams_in_citation"])
            num_bigrams_in_selfciting.append(row["num_bigrams_in_citation"])  
        
            self_cit += 1
           
        elif row["Selfcitation"] == 0:
            if row["Inclusion Reduced Linkage Unigrams"] != 0:
                preclusive_incl_unigram_red_linkage.append(1/row["Inclusion Reduced Linkage Unigrams"])
            else: preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
            
            if row["Inclusion Complete Linkage Unigrams"] != 0:  
                preclusive_incl_unigram_compl_linkage.append(1/row["Inclusion Complete Linkage Unigrams"])
            else: preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
            
            if row["Inclusion Reduced Linkage Bigrams"] != 0:         
                preclusive_incl_bigram_red_linkage.append(1/row["Inclusion Reduced Linkage Bigrams"])
            else: preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
            
            if row["Inclusion Complete Linkage Bigrams"] !=0:
                preclusive_incl_bigram_compl_linkage.append(1/row["Inclusion Complete Linkage Bigrams"])
            else: preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
            
            num_unique_unigrams_in_otherciting.append(row["num_unique_unigrams_in_citation"])
            num_unigrams_in_otherciting.append(row["num_unigrams_in_citation"])
            num_unique_bigrams_in_otherciting.append(row["num_unique_bigrams_in_citation"])
            num_bigrams_in_otherciting.append(row["num_bigrams_in_citation"])    
            nonself_cit += 1
    
    if len(cumulative_incl_unigram_red_linkage) == 0:
        mean_cumulative_incl_unigram_red_linkage.append(0)
        mean_cumulative_incl_unigram_compl_linkage.append(0)
        mean_cumulative_incl_bigram_red_linkage.append(0)
        mean_cumulative_incl_bigram_compl_linkage.append(0)
    else:
        mean_cumulative_incl_unigram_red_linkage.append(mean(cumulative_incl_unigram_red_linkage))
        mean_cumulative_incl_unigram_compl_linkage.append(mean(cumulative_incl_unigram_compl_linkage))
        mean_cumulative_incl_bigram_red_linkage.append(mean(cumulative_incl_bigram_red_linkage))
        mean_cumulative_incl_bigram_compl_linkage.append(mean(cumulative_incl_bigram_compl_linkage))   

    if len(preclusive_incl_unigram_red_linkage) == 0:
        mean_preclusive_incl_unigram_red_linkage.append(promote_prec_unigram_red_linkage)
        mean_preclusive_incl_unigram_compl_linkage.append(promote_prec_unigram_compl_linkage)
        mean_preclusive_incl_bigram_red_linkage.append(promote_prec_bigram_red_linkage)
        mean_preclusive_incl_bigram_compl_linkage.append(promote_prec_bigram_compl_linkage)
        
    else:
        mean_preclusive_incl_unigram_red_linkage.append(mean(preclusive_incl_unigram_red_linkage))
        mean_preclusive_incl_unigram_compl_linkage.append(mean(preclusive_incl_unigram_compl_linkage))
        mean_preclusive_incl_bigram_red_linkage.append(mean(preclusive_incl_bigram_red_linkage))
        mean_preclusive_incl_bigram_compl_linkage.append(mean(preclusive_incl_bigram_compl_linkage))   

df = pd.DataFrame(data = patent_id)  

df["Assignee Name"] = assignee_name
df["Micron"] = micron
df["IBM"] = ibm
df["Samsung"] = samsung
df["Toshiba"] = toshiba

#dependent variables
#cumulative

#mean
df["mean_cumulative_incl_unigram_red_linkage"] =mean_cumulative_incl_unigram_red_linkage

df["mean_cumulative_incl_unigram_compl_linkage"] =mean_cumulative_incl_unigram_compl_linkage

df["mean_cumulative_incl_bigram_red_linkage"] =mean_cumulative_incl_bigram_red_linkage

df["mean_cumulative_incl_bigram_compl_linkage"] =mean_cumulative_incl_bigram_compl_linkage


#preclusive

#mean
df["mean_preclusive_incl_unigram_red_linkage"] =mean_preclusive_incl_unigram_red_linkage

df["mean_preclusive_incl_unigram_compl_linkage"] =mean_preclusive_incl_unigram_compl_linkage

df["mean_preclusive_incl_bigram_red_linkage"] =mean_preclusive_incl_bigram_red_linkage

df["mean_preclusive_incl_bigram_compl_linkage"] =mean_preclusive_incl_bigram_compl_linkage


df["filing_year"] = filing_year
df["grant_year"] = grant_year

df.rename(columns={0:"PN"}, inplace=True)
df.to_excel("All_aggregated_inverse.xlsx", index=False)       
df.to_csv("All_aggregated_inverse.csv", sep=";", decimal=",")