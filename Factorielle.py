#!/usr/bin/env python
# coding: utf-8

# In[1]:


def factorielle(n):
    if n==0:
        return 1
    else:
        x = 1
        for k in range(2,n+1):
            x=x*k
        return x

    
factorielle(5)

