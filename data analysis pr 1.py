#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import pandas as pd


# In[4]:


import seaborn as sns


# In[7]:


data = pd.read_csv(r"C:\Users\Lenovo\Documents\shopping_trends.csv", encoding= 'unicode_escape')


# In[14]:


data.head(10)


# In[15]:


data.shape
data.tail


# In[11]:


data.describe()


# In[13]:


data.info()


# In[16]:


data.describe


# In[17]:


data.describe()


# In[18]:


data.columns


# In[19]:


data.nunique()


# In[20]:


data['Gender'].unique()


# In[23]:


data['Item Purchased'].unique()


# In[24]:


data['Category'].unique()


# In[25]:


data.isnull().sum()


# In[26]:


data = data.drop(data.columns[0],axis = 1)
data             


# In[27]:


dupli = sum(data.duplicated())
dupli


# In[28]:


len(data.index)


# In[29]:


print(dupli/len(data.index)*100)


# In[30]:


showdup = data[data.duplicated()]
showdup


# In[31]:


dupli = sum(data.duplicated())
dupli


# In[33]:


display(data.info())


# In[35]:


null = data[data.isna().any(axis=1)]
null


# In[36]:


data = data.dropna()
display(data.info())


# In[37]:


correlation = data.corr()


# In[39]:


pd.isnull(data).sum()


# In[41]:


data['Review Rating'] = data['Review Rating'].astype('int')


# In[42]:


data['Review Rating'].dtypes


# In[43]:


data.columns


# In[50]:


sales_generate = data.groupby(['Gender'], as_index=False)['Purchase Amount (USD)'].sum().sort_values(by='Purchase Amount (USD)',ascending=False)
sns.barplot(x='Gender',y='Purchase Amount (USD)',data=sales_generate)


# In[52]:


sales_generate = data.groupby(['Payment Method'], as_index=False)[].sum().sort_values(by='Shipping Type',ascending=False)
sns.barplot(x='Payment Method',y='Shipping Type',data=sales_generate)


# In[55]:


data.columns


# In[56]:


correlation = data.corr()


# In[57]:


sns.pairplot(data)


# In[59]:


data.columns


# In[63]:


sns.histplot(data['Review Rating'], bins = 5)


# In[64]:


data.columns


# In[67]:


sns.catplot(x= 'Discount Applied', kind = 'box',df = data)


# In[ ]:




