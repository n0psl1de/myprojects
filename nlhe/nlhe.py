#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
import pandas as pd


# In[4]:


deck_num = []

ranks_num = ['01','02','03','04','05','06','07','08','09','10','11','12','13']
suits_num = ['14','15','16','17']

[deck_num.append(x+y) for x in ranks_num for y in suits_num]
print(deck_num)


# In[5]:


suits = ['s','c','d','h']
ranks = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
deck_str =[]
[deck_str.append(x+y) for x in ranks for y in suits]

print(deck_str)


# In[6]:


deck_dict = dict(zip(deck_num,deck_str))
print(deck_dict)


# In[7]:


print(list(deck_dict.keys()))


# In[8]:


print(list(deck_dict.values()))


# In[11]:


# Get random sample from deck_dict

for i in range(0,2):
    s = random.sample(list(deck_dict),10)
    dict_sample = {k: deck_dict[k] for k in s}
    print("Hand",i+1)
    print(list(dict_sample.values()),"\n")
    print(dict_sample,"\n")


# In[12]:


dict_sample


# In[13]:


def is_hc(cards_dealt):
    for i in deals:
        print(i)
    
is_hc(cards_dealt)


# In[ ]:




