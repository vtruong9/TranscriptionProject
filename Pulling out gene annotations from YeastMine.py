#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import gzip


# In[2]:


### TEST ###
# FILE = "summary38genes.csv"


# In[3]:


#for line in file:
#     line[xcount up][1]
#     print to existingSpreadsheet.xls

f = open("summary38genes.csv")
lines = f.readlines()
f.close()

alphaList = []

for l in lines:
    alphaList.append(l[5])


print(alphaList)

#def load_pdb(pdb_file):
#    
#    f = open(pdb_file,'r')
#    lines = f.readlines()
#    f.close()
#    
#    all_coord = []
#    for l in lines:
#        if l[0:4] == "ATOM" and l[13:16] == "CA ":
#            coord = [float(l[(30 + i*8):(38 + i*8)]) for i in range(3)]
#            all_coord.append(coord)
#            
#    return np.array(all_coord)


#ARE YOU SHITTING ME CSV IS JUST A STRAIGHT LIST OF CHARACTERS WHO DOES THAT?!?!?1

