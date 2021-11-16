# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 15:32:20 2021

@author: pathouli
"""

def clean_text(txt_in):
    import re
    clean = re.sub('[^A-Za-z0-9]+', " ", txt_in).strip()
    return clean

def file_seeker(path_in, sw):
    import os
    import pandas as pd
    import re
    import nltk
    dictionary = nltk.corpus.words.words("en")
    tmp_pd = pd.DataFrame()
    for dirName, subdirList, fileList in os.walk(path_in):
        tmp_dir_name = dirName.split("/")[-1::][0]
        try:
            for word in fileList:
                #print(word)
                tmp = open(dirName+"/"+word, "r", encoding="ISO-8859-1")
                tmp_f = tmp.read()
                tmp.close()
                tmp_f = re.sub('[^A-Za-z0-9]+', " ", tmp_f).strip().lower() #\n extra spacex
                if sw == "check_words":
                    tmp_f = [word for word in tmp_f.split() if word in dictionary]
                    tmp_f = ' '.join(tmp_f)
                tmp_pd = tmp_pd.append({'label': tmp_dir_name, 
                                        #'path': dirName+"/"+word}, 
                                        'body': tmp_f},
                                        ignore_index = True)
        except Exception as e:
            print (e)
            pass
    return tmp_pd

def rem_sw(var):
    from nltk.corpus import stopwords
    sw = set(stopwords.words("English"))
    my_test = [word for word in var.split() if word not in sw]
    my_test = ' '.join(my_test)
    return my_test


def check_dictionary(var):
    import nltk
    dictionary = nltk.corpus.words.words("en")
    fin_txt = [word for word in var.split() if word in dictionary]
    fin_txt = ' '.join(fin_txt)
    return fin_txt

def stem_fun(var):
    from nltk.stem.porter import PorterStemmer
    stemmer = PorterStemmer()
    tmp_txt = [stemmer.stem(word) for word in var.split()]
    tmp_txt = ' '.join(tmp_txt)
    return tmp_txt

def jaccard_fun(var_a, var_b):
    #DOCUMENT SIMILARITY
    doc_a_set = set(var_a.split())
    doc_b_set = set(var_b.split())
    j_d = float(len(doc_a_set.intersection(
        doc_b_set)))/ float(len(doc_a_set.union(doc_b_set)))
    return j_d

# def file_seeker(path_in):
#     import os
#     import pandas as pd
#     tmp_pd = pd.DataFrame()
#     for dirName, subdirList, fileList in os.walk(path_in):
#         tmp_dir_name = dirName.split("/")[-1::][0]
#         for word in fileList:
#             try:
#                 tmp_pd = tmp_pd.append(
#                     {"label": tmp_dir_name,"path": dirName+"/"+word},
#                     ignore_index=True)
#             except Exception as e:
#                 print (e)
#                 pass
#     return tmp_pd
