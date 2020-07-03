#!/usr/bin/env python
# coding: utf-8

# # Desafio 1
# 
# Para esse desafio, vamos trabalhar com o data set [Black Friday](https://www.kaggle.com/mehdidag/black-friday), que reúne dados sobre transações de compras em uma loja de varejo.
# 
# Vamos utilizá-lo para praticar a exploração de data sets utilizando pandas. Você pode fazer toda análise neste mesmo notebook, mas as resposta devem estar nos locais indicados.
# 
# > Obs.: Por favor, não modifique o nome das funções de resposta.

# ## _Set up_ da análise

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


black_friday = pd.read_csv("black_friday.csv")


# ## Inicie sua análise a partir daqui

# In[ ]:





# ## Questão 1
# 
# Quantas observações e quantas colunas há no dataset? Responda no formato de uma tuple `(n_observacoes, n_colunas)`.

# In[8]:


def q1():
    return black_friday.shape


# ## Questão 2
# 
# Há quantas mulheres com idade entre 26 e 35 anos no dataset? Responda como um único escalar.

# In[9]:


def q2():
    return black_friday.query("Gender == 'F' & Age == '26-35'").shape[0]


# ## Questão 3
# 
# Quantos usuários únicos há no dataset? Responda como um único escalar.

# In[4]:


def q3():
    return len(black_friday['User_ID'].unique())


# ## Questão 4
# 
# Quantos tipos de dados diferentes existem no dataset? Responda como um único escalar.

# In[7]:


def q4():
   return len(black_friday.dtypes.unique())


# ## Questão 5
# 
# Qual porcentagem dos registros possui ao menos um valor null (`None`, `ǸaN` etc)? Responda como um único escalar entre 0 e 1.

# In[2]:


def q5():
    return black_friday[black_friday.Product_Category_2.isna()|black_friday.Product_Category_3.isna()].shape[0]/len(black_friday) 


# ## Questão 6
# 
# Quantos valores null existem na variável (coluna) com o maior número de null? Responda como um único escalar.

# In[6]:


def q6():
   return black_friday["Product_Category_3"].isna().sum()


# ## Questão 7
# 
# Qual o valor mais frequente (sem contar nulls) em `Product_Category_3`? Responda como um único escalar.

# In[10]:


def q7():
   return black_friday.Product_Category_3.mode()[0]


# ## Questão 8
# 
# Qual a nova média da variável (coluna) `Purchase` após sua normalização? Responda como um único escalar.

# In[10]:


def q8():
    MinMaxUp = (black_friday[['Purchase']] - black_friday[['Purchase']].min(axis=0))
    MinMaxDown = (black_friday[['Purchase']].max(axis=0) - black_friday[['Purchase']].min(axis=0))
    MinMaxNormalized = MinMaxUp / MinMaxDown
    return MinMaxNormalized.mean()[0].item()


# ## Questão 9
# 
# Quantas ocorrências entre -1 e 1 inclusive existem da variáel `Purchase` após sua padronização? Responda como um único escalar.

# In[5]:


def q9():
   Purchase = black_friday.Purchase
   Padronizacao = (Purchase - Purchase.mean()) / (Purchase.std())
   return int(Padronizacao.between(-1, 1).sum())


# ## Questão 10
# 
# Podemos afirmar que se uma observação é null em `Product_Category_2` ela também o é em `Product_Category_3`? Responda com um bool (`True`, `False`).

# In[8]:


def q10():
    return black_friday["Product_Category_2"].isna().equals(black_friday["Product_Category_2"].isna())


# In[ ]:




