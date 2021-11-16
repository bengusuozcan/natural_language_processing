# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 19:03:54 2021
@author: Bengusu Ozcan

1) From hw1.pkl dataframe, read 3 columns: "body_basic", "lower", "sw"
2) Create a dictionary called corpus_analytics whose keys represent each column name above and the value is a pandas dataframe
3) Each of these pandas dataframes consists of three columns:
   - token - each row represents a unique token(word)
   - raw_frequency - total number of times the specific token shows
   - probability(%) - out of the count of all tokens (non-unique) what % of times does this word show up? 
4) Sort the each pandas dataframe by "raw_frequency" in descending order

"""

import pickle
import pandas as pd
the_data = pickle.load(open("hw1.pkl", "rb"))


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
