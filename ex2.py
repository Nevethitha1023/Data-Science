#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[28]:


df=pd.read_csv(r"C:\Users\Lenovo\Downloads\housing_dataset.csv")


# In[29]:


df


# In[30]:


df.isnull()


# In[31]:


df['Price']=df['Price'].fillna(df['Price'].median())


# In[32]:


df['Bathrooms']=df['Bathrooms'].fillna(df['Bathrooms'].mean())


# In[33]:


df=df.dropna(axis=0)


# In[34]:


df


# In[35]:


Q1 = df['Price'].quantile(0.25)
Q3 = df['Price'].quantile(0.75)
IQR = Q3 - Q1


# In[43]:


lb=Q1-1.5*IQR
ub=Q3+1.5*IQR


# In[44]:


outlier=((df[['Price']]<lb) | (df[['Price']]>ub)).any(axis=1)


# In[45]:


clean_data = df[~outlier]


# In[46]:


clean_data


# In[60]:


clean_data['Sqft_Living']= (clean_data['Sqft_Living']-clean_data['Sqft_Living'].min())/(clean_data['Sqft_Living'].max()-clean_data['Sqft_Living'].min())


# In[61]:


clean_data


# In[62]:


clean_data['Year_Built'].astype(int)


# In[63]:


dummie=pd.get_dummies(clean_data['Waterfront'],drop_first=True)


# In[67]:


dummie


# In[69]:


data=pd.concat([clean_data,dummie],axis=1)


# In[70]:


data


# In[71]:


data.to_csv('ex2.csv')


# In[ ]:




