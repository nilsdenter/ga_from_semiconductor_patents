# Measuring generative appropriability: Experiments with US semiconductor patents

This project contains the data and code used in the paper titled "Measuring generative appropriability: Experiments with US semiconductor patents". 

To reproduce our results, first, you need to download all files from the data folder and unwrap if wrapped.

Then, the code must be executed in ascending order of the sequence number.

The code "01_Match_Patent_Citations.py" transforms the retrieved patents and patent citations of all four semiconductor firms in better format and identifies whether a patent citation comes from the same applicant firm or from others. As result, the code creates for each firm an excel file containing patents and their citations as well as information on applicants.

The code "02_Calculate_Knowledge_Flow.py" uses the information from code 01 and calculates the knowledge flow between patent citation pairs. To do this, the titles, abstracts and claims of all patents and patent citations are retrieved and pre-processed. Then, for each pair, the four different formulae (reduced linkage or complete linkage & unigrams or bigrams) are calculated. As result, the code creates a csv file containing all patent citation pairs with their corresponding knowledge flow values of the four different variants.

The code "03_Identify_Patent_Family_Membership.py" identifies whether the patents of a patent citation pair belong to the same patent family. For this code, the user needs to download data the "rel_app_text.tsv" file from https://patentsview.org/download/data-download-tables first. As result, the code expands the prior created csv file by another column indicating whether (=1) or not (=0) a patent citation pair belongs to the same patent family.

Then, the code "04_Knowledge_flow_by_patent_family_membership.py" performs statistical t-tests to test whether there is a significant difference in knowledge flow between patent citation pairs that belong to the same patent family and patent citation pairs that does not. The results can be obtained from the Results folder, file "Table 2 Independent sample t-tests of knowledge flow by patent family.txt".

The code "05_Knowledge_flow_by_time_lag.py" performs the second knowledge flow analysis. The code plots the mean and 95% confidence interval knowledge flow by time lag in filing years between the cited and the citing patent. The results can be obtained from the Results folder, file "Figure 3 Knowledge Flow by Time Lag.svg".

The code "06_Calculate_cumulative_and_preclusive_GA.py" computes the cumulative and preclusive GA values according to the formulae in the paper for each patent. As result, the code creates a csv file containing all patents and their corresponding cumulative and preclusive GA value for each of the four variants.

Finally, the code "07_GA_in_time.py" plots the different cumulative and preclusive GA values per filing year for each of the four semiconductor firms in a scatter-like plot. The results can be obtained from the Results folder, file "Figure 4 Generative Appropriability by Filing Year.svg". 

Please see the paper for further information.
