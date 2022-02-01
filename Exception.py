#!/usr/bin/env python
# coding: utf-8

# In[13]:


def Polynomee(x):
  try:
      x=int(input("Rentrez un Chiffre : "))
      if x<0:
        print("Veuillez rentrez un chiffre positif")
        Polynomee(x)
      elif 0<x<1:
        print("ce nombre est trop petit")
        Polynomee(x)
      elif x>9999999999999:
        print("ce nombre est trop grand")
        Polynomee(x)
      else:
        resultat = (x*x*x)-1.5*(x*x)-6*x+5
        print("Le resultat est", resultat)
  except ValueError:
    print("Désolé, la valeure saisie n'est pas un nombre")
  except TypeError:
    print("il y a eu une erreur dans le type")

Polynomee(9)


# In[ ]:




