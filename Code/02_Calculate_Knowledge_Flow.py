from nltk.util import skipgrams
import regex as re
import pandas as pd
import regex
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
import nltk
nltk.download('punkt')
from time import time
t0 = time()

def create_stopword_list():
    fox_stoplist = list(set(pd.read_csv("stopwords_fox.csv", index_col=0).index))
    stopwords_from_uspto = list(set(pd.read_csv("stopwords_uspto.csv", index_col=0).index))
    stopwords_arts = list(set(pd.read_csv("stopwords_specific_Arts.csv", index_col=0).index))
    stopwords_technet = list(set(pd.read_csv("stopwords_technet.csv", index_col=0).index))
    stoplist = set(stopwords_technet + stopwords_arts + stopwords.words('english') + fox_stoplist + stopwords_from_uspto)
    return stoplist
stoplist = create_stopword_list()

def tokenization_and_preprocessing(raw_patent):
    #remove numbers
    raw_patent = re.sub(r'\P{L}+', ' ', raw_patent)
    #remove special characters
    raw_patent = re.sub('[^A-ZÜÖÄa-z0-9]+', ' ', raw_patent)
    raw_patent = raw_patent.replace("."," ") 
    raw_patent = raw_patent.replace(","," ") 
    raw_patent = raw_patent.replace("!"," ") 
    raw_patent = raw_patent.replace("?"," ") 
    raw_patent = raw_patent.replace("&"," ") 
    raw_patent = raw_patent.replace("-"," ")
    raw_patent = raw_patent.replace(";"," ") 
    raw_patent = raw_patent.replace("/"," ")
    raw_patent = raw_patent.replace(")"," ") 
    raw_patent = raw_patent.replace("("," ")
    raw_patent = raw_patent.replace("+"," ") 
    raw_patent = raw_patent.replace("="," ")
    raw_patent = raw_patent.replace("\\"," ")
    raw_patent = raw_patent.replace(":"," ")
    raw_patent = raw_patent.replace("'"," ") 
    raw_patent = raw_patent.replace("`"," ") 
    raw_patent = raw_patent.replace("´"," ")
    raw_patent = raw_patent.replace("#"," ")
    #remove numbers
    raw_patent = regex.sub(r'\P{L}+', ' ', raw_patent)
    #transform words into lower case and into a list
    texts = raw_patent.lower().split()
    #remove stop words
    texts = [word for word in texts if len(word) >= 3]
    texts = [word for word in texts if not word.isdigit()]
    texts = [word for word in texts if word not in stoplist]
    #stemming
    #Porter stemmer based on Porter, M. “An algorithm for suffix stripping.” Program 14.3 (1980): 130-137.
    porter_stemmer = PorterStemmer(mode='NLTK_EXTENSIONS')
    texts = [porter_stemmer.stem(word) for word in texts]
    return texts

def inclusion_reduced_linkage(origin, successive):
    patent_1 = set(origin)
    patent_2 = set(successive)
    ci = len(patent_1)
    cij = 0
    if len(patent_1) == 0 or len(patent_2) == 0:
        inclusion = 0
    else:
        for word in patent_1:
            if word in patent_2:
                cij += 1        
        inclusion = cij/ci
    return inclusion#, cij, ci

def inclusion_complete_linkage(origin, successive):
    #similar to reduced linkage inclusion
    patent_1 = origin
    patent_1.sort()
    patent_2 = set(successive)
    ci = len(patent_1)
    cij = 0
    if len(patent_1) == 0 or len(patent_2) == 0:
        inclusion = 0
    else:
        for word1 in patent_1:
            if word1 in patent_2:
                cij += 1        
        inclusion = cij/ci
    return inclusion#, cij, ci

def create_bigrams(tokens, window):
    #create bigrams
    bigrams = skipgrams(tokens,2,window-2)
    tac = []
    for bigram in bigrams:
        bigram = list(bigram)
        if bigram[0] == bigram[1]:
            continue
        bigram.sort()
        bigram = " ".join(bigram)
        tac.append(bigram)
    return tac

"""""""""""""""""""""""""""

MICRON TECHNOLOGY

"""""""""""""""""""""""""""

patents_tac = pd.read_csv("Micron_Technology_and_Citations_TAC_01.tsv", sep = '\t', header = 0,  lineterminator='\r').dropna()
patents_tac_02 = pd.read_csv("Micron_Technology_and_Citations_TAC_02.tsv", sep = '\t', header = 0,  lineterminator='\r').dropna()
patents_tac = patents_tac.append(patents_tac_02)
del patents_tac_02

#improve data
pn = []
for index, row in patents_tac.iterrows():
    patentnr = row["PN"] 
    
    pn.append(int(patentnr))
patents_tac["PN"] = pn
patents_tac.set_index("PN", inplace=True)

citation_data1 = pd.read_excel("Micron_Citations.xlsx", engine = "openpyxl")

incl_unigram_red_linkage = []
incl_unigram_compl_linkage = []
incl_bigram_red_linkage = []
incl_bigram_compl_linkage = []


application_year = []
issue_year = []

counter = 1
t1 = time()
for index, row in citation_data1.iterrows():
    #preprocess title, abstract and claims of focal patent
    focal_patent = row["Focal_Patent"]
    tac_focal_patent = patents_tac.loc[focal_patent,:]
    citing_patent = row["Citation"]
    tac_citing_patent = patents_tac.loc[citing_patent,:]
    application_year.append(int(tac_focal_patent["APD"][6:10]))
    issue_year.append(int(tac_focal_patent["ISD"][6:10]))
    
    tac_focal_patent = tac_focal_patent["TTL"] + " " + tac_focal_patent["ABST"] + " " + tac_focal_patent["ACLM"]
    tac_focal_patent = tokenization_and_preprocessing(tac_focal_patent)  
        
    #preprocess title, abstract and claims of citing patent
    tac_citing_patent = tac_citing_patent["TTL"] + " " + tac_citing_patent["ABST"] + " " + tac_citing_patent["ACLM"]
    tac_citing_patent = tokenization_and_preprocessing(tac_citing_patent)

    incl_unigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_unigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    
    tac_focal_patent = create_bigrams(tokens=tac_focal_patent, window=4)
    tac_citing_patent = create_bigrams(tokens=tac_citing_patent, window=4)
    incl_bigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_bigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
        
    if counter%2000==0:
        print("\nNext 2,000 patents finished in {0} seconds {1}/{2}.".format(int(time()-t1), counter, len(citation_data1)))
        t1 = time()
    counter += 1

citation_data1["Inclusion Reduced Linkage Unigrams"] = incl_unigram_red_linkage
citation_data1["Inclusion Complete Linkage Unigrams"] = incl_unigram_compl_linkage
citation_data1["Inclusion Reduced Linkage Bigrams"] = incl_bigram_red_linkage
citation_data1["Inclusion Complete Linkage Bigrams"] = incl_bigram_compl_linkage
citation_data1["Appl Year Focal Patent"] = application_year
citation_data1["Grant Year Focal Patent"] = issue_year

citation_data1.to_excel("Micron_inclusion_paired.xlsx", index=False)

"""""""""""""""""""""""""""

IBM

"""""""""""""""""""""""""""

patents_tac = pd.read_csv("IBM_and_Citations_TAC.tsv", sep = '\t', header = 0,  lineterminator='\r').dropna()
#improve data
pn = []
for index, row in patents_tac.iterrows():
    patentnr = row["PN"]
    patentnr = patentnr.strip()
    pn.append(int(patentnr))
patents_tac["PN"] = pn
patents_tac.set_index("PN", inplace=True)

citation_data2 = pd.read_excel("IBM_Citations.xlsx", engine = "openpyxl")

incl_unigram_red_linkage = []
incl_unigram_compl_linkage = []
incl_bigram_red_linkage = []
incl_bigram_compl_linkage = []

application_year = []
issue_year = []

counter = 1
t1 = time()
for index, row in citation_data2.iterrows():
    #preprocess title, abstract and claims of focal patent
    focal_patent = row["Focal_Patent"]
    tac_focal_patent = patents_tac.loc[focal_patent,:]
    application_year.append(int(tac_focal_patent["APD"][6:10]))
    issue_year.append(int(tac_focal_patent["ISD"][6:10]))

    tac_focal_patent = tac_focal_patent["TTL"] + " " + tac_focal_patent["ABST"] + " " + tac_focal_patent["ACLM"]
    tac_focal_patent = tokenization_and_preprocessing(tac_focal_patent)

    #preprocess title, abstract and claims of citing patent
    citing_patent = row["Citation"]
    tac_citing_patent = patents_tac.loc[citing_patent,:]
    tac_citing_patent = tac_citing_patent["TTL"] + " " + tac_citing_patent["ABST"] + " " + tac_citing_patent["ACLM"]
    tac_citing_patent = tokenization_and_preprocessing(tac_citing_patent)
    
    incl_unigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_unigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    
    tac_focal_patent = create_bigrams(tokens=tac_focal_patent, window=4)
    tac_citing_patent = create_bigrams(tokens=tac_citing_patent, window=4)  
    incl_bigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_bigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
        
    if counter%2000==0:
        print("\nNext 2,000 patents finished in {0} seconds {1}/{2}.".format(int(time()-t1), counter, len(citation_data2)))
        t1 = time()
    counter += 1

citation_data2["Inclusion Reduced Linkage Unigrams"] = incl_unigram_red_linkage
citation_data2["Inclusion Complete Linkage Unigrams"] = incl_unigram_compl_linkage
citation_data2["Inclusion Reduced Linkage Bigrams"] = incl_bigram_red_linkage
citation_data2["Inclusion Complete Linkage Bigrams"] = incl_bigram_compl_linkage

citation_data2["Appl Year Focal Patent"] = application_year
citation_data2["Grant Year Focal Patent"] = issue_year

citation_data2.to_excel("IBM_inclusion_paired.xlsx", index=False)

"""""""""""""""""""""""""""

SAMSUNG

"""""""""""""""""""""""""""

patents_tac = pd.read_csv("Samsung_and_Citations_TAC.tsv", sep = '\t', header = 0,  lineterminator='\r').dropna()
#improve data
pn = []
for index, row in patents_tac.iterrows():
    patentnr = row["PN"]
    
    pn.append(int(patentnr))
patents_tac["PN"] = pn
patents_tac.set_index("PN", inplace=True)

citation_data3 = pd.read_excel("Samsung_Citations.xlsx", engine = "openpyxl")

incl_unigram_red_linkage = []
incl_unigram_compl_linkage = []
incl_bigram_red_linkage = []
incl_bigram_compl_linkage = []

application_year = []
issue_year = []

counter = 1
t1 = time()
for index, row in citation_data3.iterrows():
    #preprocess title, abstract and claims of focal patent
    focal_patent = row["Focal_Patent"]
    tac_focal_patent = patents_tac.loc[focal_patent,:]
    citing_patent = row["Citation"]
    tac_citing_patent = patents_tac.loc[citing_patent,:]
    application_year.append(int(tac_focal_patent["APD"][6:10]))
    issue_year.append(int(tac_focal_patent["ISD"][6:10]))

    tac_focal_patent = tac_focal_patent["TTL"] + " " + tac_focal_patent["ABST"] + " " + tac_focal_patent["ACLM"]
    tac_focal_patent = tokenization_and_preprocessing(tac_focal_patent)

    #preprocess title, abstract and claims of citing patent
    tac_citing_patent = tac_citing_patent["TTL"] + " " + tac_citing_patent["ABST"] + " " + tac_citing_patent["ACLM"]
    tac_citing_patent = tokenization_and_preprocessing(tac_citing_patent)
    
    incl_unigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_unigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    
    tac_focal_patent = create_bigrams(tokens=tac_focal_patent, window=4)
    tac_citing_patent = create_bigrams(tokens=tac_citing_patent, window=4)
    
    incl_bigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_bigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
        
    if counter%2000==0:
        print("\nNext 2,000 patents finished in {0} seconds {1}/{2}.".format(int(time()-t1), counter, len(citation_data3)))
        t1 = time()
    counter += 1

citation_data3["Inclusion Reduced Linkage Unigrams"] = incl_unigram_red_linkage
citation_data3["Inclusion Complete Linkage Unigrams"] = incl_unigram_compl_linkage
citation_data3["Inclusion Reduced Linkage Bigrams"] = incl_bigram_red_linkage
citation_data3["Inclusion Complete Linkage Bigrams"] = incl_bigram_compl_linkage


citation_data3["Appl Year Focal Patent"] = application_year
citation_data3["Grant Year Focal Patent"] = issue_year

citation_data3.to_excel("Samsung_inclusion_paired.xlsx", index=False)

"""""""""""""""""""""""""""

TOSHIBA

"""""""""""""""""""""""""""

patents_tac = pd.read_csv("Toshiba_and_Citations_TAC.tsv", sep = '\t', header = 0,  lineterminator='\r').dropna()
#improve data
pn = []
for index, row in patents_tac.iterrows():
    patentnr = row["PN"] 
    
    pn.append(int(patentnr))
patents_tac["PN"] = pn
patents_tac.set_index("PN", inplace=True)

citation_data4 = pd.read_excel("Toshiba_Citations.xlsx", engine = "openpyxl")

incl_unigram_red_linkage = []
incl_unigram_compl_linkage = []
incl_bigram_red_linkage = []
incl_bigram_compl_linkage = []

application_year = []
issue_year = []

counter = 1
t1 = time()
for index, row in citation_data4.iterrows():
    #preprocess title, abstract and claims of focal patent
    focal_patent = row["Focal_Patent"]
    tac_focal_patent = patents_tac.loc[focal_patent,:]
    citing_patent = row["Citation"]
    tac_citing_patent = patents_tac.loc[citing_patent,:]
    application_year.append(int(tac_focal_patent["APD"][6:10]))
    issue_year.append(int(tac_focal_patent["ISD"][6:10]))
    
    tac_focal_patent = tac_focal_patent["TTL"] + " " + tac_focal_patent["ABST"] + " " + tac_focal_patent["ACLM"]
    tac_focal_patent = tokenization_and_preprocessing(tac_focal_patent)
    
    #preprocess title, abstract and claims of citing patent
    tac_citing_patent = tac_citing_patent["TTL"] + " " + tac_citing_patent["ABST"] + " " + tac_citing_patent["ACLM"]
    tac_citing_patent = tokenization_and_preprocessing(tac_citing_patent)
    
    incl_unigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_unigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    
    tac_focal_patent = create_bigrams(tokens=tac_focal_patent, window=4)
    tac_citing_patent = create_bigrams(tokens=tac_citing_patent, window=4)

    incl_bigram_red_linkage.append(inclusion_reduced_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
    incl_bigram_compl_linkage.append(inclusion_complete_linkage(origin=tac_focal_patent,successive=tac_citing_patent))
        
    if counter%2000==0:
        print("\nNext 2,000 patents finished in {0} seconds {1}/{2}.".format(int(time()-t1), counter, len(citation_data4)))
        t1 = time()
    counter += 1

citation_data4["Inclusion Reduced Linkage Unigrams"] = incl_unigram_red_linkage
citation_data4["Inclusion Complete Linkage Unigrams"] = incl_unigram_compl_linkage
citation_data4["Inclusion Reduced Linkage Bigrams"] = incl_bigram_red_linkage
citation_data4["Inclusion Complete Linkage Bigrams"] = incl_bigram_compl_linkage


citation_data4["Appl Year Focal Patent"] = application_year
citation_data4["Grant Year Focal Patent"] = issue_year

citation_data4.to_excel("Toshiba_inclusion_paired.xlsx", index=False)

"""""""""""""""""""""""""""

CREATE ONE TABLE CONTAINING EACH TABLE OF THE FOUR FIRMS

"""""""""""""""""""""""""""

citation_data1 = citation_data1.append(citation_data2)
citation_data1 = citation_data1.append(citation_data3)
citation_data1 = citation_data1.append(citation_data4)
del citation_data2, citation_data3, citation_data4

micron = []
ibm = []
samsung = []
toshiba = []

for index, row in citation_data1.iterrows():
    if row["Assignee_Focal_Patent"] == "Micron Technology":
        micron.append(1)
    else:
        micron.append(0)
        
    if row["Assignee_Focal_Patent"] == "IBM":
        ibm.append(1)
    else:
        ibm.append(0)
        
    if row["Assignee_Focal_Patent"] == "Samsung":
        samsung.append(1)
    else:
        samsung.append(0)
    if row["Assignee_Focal_Patent"] == "Toshiba":
        toshiba.append(1)
    else:
        toshiba.append(0)
citation_data1["IBM"] = ibm
citation_data1["Toshiba"] = toshiba
citation_data1["Micron"] = micron
citation_data1["Samsung"] = samsung

#citation_data1.to_excel("All_inclusion_paired.xlsx", index=False)
citation_data1.to_csv("All_inclusion_paired.csv", sep=";", index=False)