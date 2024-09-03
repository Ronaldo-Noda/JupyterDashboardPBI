#!/usr/bin/env python
# coding: utf-8

# In[38]:


#Versão da Linguagem Python

from platform import python_version
print ("Versão da Linguagem Python usada neste Jupyter Notebook: ", python_version())


# In[5]:


#Imports

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import os
os.environ["OMP_NUM_THREADS"] = "2"

from sklearn.cluster import KMeans
from threadpoolctl import threadpool_limits


# In[6]:


#Carregando Dados

df_dsa = pd.read_csv(r'C:\Users\ronaldo.noda\Documents\Data Science Academy - Curso PBI\Capitulo 16\dados\dados_clientes.csv')


# In[7]:


#Visuzalizando as 10 primeiras linhas

df_dsa.head(10)


# In[8]:


#Resumo Estatistico

df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']].describe() 


# In[9]:


#Criar o padronizador de dados

padronizador = StandardScaler()


# In[10]:


#Aplicar o padronizador somente nas colunas de interesse

dados_padronizados = padronizador.fit_transform(df_dsa[['idade', 'renda_anual', 'pontuacao_gastos']])


# In[11]:


#Visualizar dados padronizados

print(dados_padronizados)


# In[12]:


#Definindo número de clusters (k)

k = 3


# In[13]:


#Corrigindo erro do K-Means

with threadpool_limits(limits=2, user_api='blas'):
    from sklearn.cluster import KMeans
    kmeans = KMeans(n_clusters=k)
    kmeans.fit(dados_padronizados)


# In[14]:


#Criando modelo K-Means

kmeans = KMeans(n_clusters = k)


# In[15]:


#Treinamento do modelo com os dados padronizados

kmeans.fit(dados_padronizados)


# In[16]:


df_dsa['cluster'] = kmeans.labels_


# In[17]:


df_dsa.head(10)


# In[18]:


df_dsa.to_csv(r'C:\Users\ronaldo.noda\Documents\Data Science Academy - Curso PBI\Capitulo 16\dados\dados_clientes.csv', index = False)


# In[45]:


#Instalando pacote Power BI

get_ipython().system('pip install -q powerbiclient')


# In[51]:


#Carrega as funções usadas para autenticar e gerar relatórios

from powerbiclient import QuickVisualize, get_dataset_config, Report
from powerbiclient.authentication import DeviceCodeLoginAuthentication 


# In[53]:


#Define a autenticação no Power BI Service

device_auth = DeviceCodeLoginAuthentication()


# In[72]:


#Criar relatório no Power BI

relatorio_PBI = QuickVisualize(get_dataset_config(df_dsa), auth = device_auth)


# In[74]:


#Renderiza(Visualiza) o relatório

relatorio_PBI


# In[ ]:




