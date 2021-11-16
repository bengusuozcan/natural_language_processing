# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:03:54 2021
HW1
@author: bengu
"""

import pickle
import pandas as pd
the_data = pickle.load(open("hw1.pkl", "rb"))

#QUESTION 1

corpus_analytics = dict()
for word in the_data.columns:
    tmp_data = the_data[word].str.cat()
    corpus_data = {word:tmp_data.split().count(word) for word in set(tmp_data.split())}
corpus_data = pd.DataFrame(
{"token": corpus_data.keys(),
"raw_frequency": corpus_data.values()})
corpus_data["probability(%)"] = (corpus_data.raw_frequency / len(
tmp_data.split())) * 100
corpus_data = corpus_data.sort_values("raw_frequency", 
ascending=False)
corpus_analytics[word] = corpus_data

#QUESTION 2
"body_basic - unable to acsertain as top 10 words are common words"
"lower - seems like entomoly as it was the only uncommon word present in 
the top 10"
"sw - clearly entomology/insects"
