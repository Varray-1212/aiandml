#!/usr/bin/env python
# coding: utf-8

# In[2]:


from numpy import random
print(random.randint(1,100))
print(random.rand())


# In[5]:


print(random.randint(100,size=(3,4,2)))


# In[6]:


a=random.randint(100,size=(3))
a


# In[7]:


random.choice(a)


# In[8]:


random.choice([1,2,3,4,5,6,7,8,9],size=(3,4))


# ### pandas 
# 1. data manipulation,analysis and cleaning
# 2. tabular data,unlabelled data

# ### creating data frame
# 1. using 2 dictionaries

# In[9]:


import pandas as pd
import numpy as np
dict1={'a':1,'b':2,'c':3,'d':4,'e':5}
dict2={'a':5,'b':6,'c':7,'d':8,'e':9}
data={'first':dict1,'second':dict2}
pd.DataFrame(data)


# In[15]:


d1={'name':['varun1','karthuk','car'],'address':['hyd','bang','chennai']}
df1=pd.DataFrame(d1)
df1


# In[25]:


#using series
s1=pd.Series([1,2,3,4,5,6,7,8,9,10])
s2=pd.Series([12.23,23.34,45.56,67.4,34.45,23.34,67.4,23])
s3=pd.Series(['a','b','c','d','e','f','g','h','i','j'])
data={'column1':s1,'column2':s2,'column3':s3}
df3=pd.DataFrame(data)
df3


# ### selecting the data from the dataframe

# In[26]:


df3["column2"]


# In[27]:


df3.loc[0:5,['column1','column2']]


# In[28]:


df3.iloc[:,0]


# In[33]:


df3.iloc[0:4,0:1]


# In[30]:


df3.shape


# In[31]:


df3.columns


# In[32]:


df3.index


# In[34]:


df3.head()


# In[35]:


df3.sample()


# In[36]:


df3.describe()


# In[ ]:





# In[ ]:




