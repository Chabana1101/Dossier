#!/usr/bin/env python
# coding: utf-8

# In[12]:


def fibonacci(x):
    a=0
    b=1
    liste=[0,1]
    for i in range(x-2):
        c=a+b
        liste.append(c)
        a=b
        b=c
    return("La suite fibonacci est : ",liste)
        
fibonacci(int(input("Entrez un nombre : ")))


# In[ ]:




