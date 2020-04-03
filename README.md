# LDA-Bengali
Determining the meaningful topics in WX format Bengali documents by using LDA

## Problem Statemnet

Given:

94 Bengali literature documents in WX format where each document contains data in the following format - 
1. The sentences (a group of words) are separated by a blank lines i.e. each blank line in the document specifies the starting of a new sentence.
2. Each non-blank line contains a word which is already POS tagged.

Task:
1. Apply machine learning tool and algorithm to find out the followings in the set of 94 
documents:
	*. The meaningful topics covered by the documents.
	*. The keywords for each of those topics.
2. Submit a report (softcopy) mentioning how you have performed this task i.e. the algorithm, code and output in detailed format.

## Contents

The assignment contains the following -

1. Assignement 2 - Machine Learning(CS-603).pdf : The report mentioning how I have performed the tasks i.e. the algorithm, code and output in detailed format.
2. Code : This folder contains
	*. data_prep.py : Code for data preparation 
	*. lda.py : Code for implementing LDA, getting output and data visualization
3. Data : This folder contains
	*. 94-documents : Dataset as provided
	*. data_A.txt : Cleaned data for LDA with all words
	*. data_N.txt : Cleaned data for LDA with nouns
	*. data_NandV.txt : Cleaned data for LDA with nouns and verbs
4. Output : This older contains output and data visualization
	*. A : Folder for data_A.txt
			LDA_A_4topics.html  
			LDA_A_4topics.txt  
			LDA_A_8topics.html  
			LDA_A_8topics.txt  
	*. N : Folder for data_N.txt
			LDA_N_3topics.html  
			LDA_N_3topics.txt  
			LDA_N_9topics.html  
			LDA_N_9topics.txt  
	*. NandV : Folder for data_NandV.txt
			LDA_NandA_3topics.html  
			LDA_NandA_3topics.txt  
			LDA_NandA_9topics.html  
			LDA_NandA_9topics.txt  

