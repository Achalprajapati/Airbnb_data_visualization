#!/usr/bin/env python
# coding: utf-8

# In[21]:


# Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go


# In[3]:


airbnb = pd.read_csv(r"C:\Users\91800\Downloads\Airbnb Dataset 19.csv")


# In[4]:


# examing the head of data
airbnb.head()


# In[10]:


airbnb.info()


# In[6]:


#checking Duplicate and Droping these values 
airbnb.duplicated().sum()
airbnb.drop_duplicates(inplace=True)


# In[7]:


airbnb.isnull().sum()


# In[8]:


#droping unnecessary cols
airbnb.drop(['name','id','host_name','last_review'], axis=1, inplace=True)


# In[10]:


#Replacing review_per_month by zero
airbnb.fillna({'reviews_per_month':0}, inplace=True)
#examing changes
airbnb.reviews_per_month.isnull().sum()


# In[11]:


#Removing Nan values from  dataframe
airbnb.isnull().sum()
airbnb.dropna(how='any',inplace=True)
airbnb.info()


# In[12]:


# checking null value
airbnb.isnull().sum()


# In[14]:


#checking the continuous values using the describe function
airbnb.describe()


# In[15]:


#checking the correlation between cols of dataframe
corr = airbnb.corr(method='kendall')
plt.figure(figsize=(15,8))
sns.heatmap(corr, annot=True)
airbnb.columns


# #### Ploting the neighbourhood_group's and cheking the count of neighbourhood_group

# In[18]:


sns.countplot(airbnb['neighbourhood_group'])
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.title('Neighbourhood Group')


# ### checking the neighbourhood

# In[25]:


sns.countplot(airbnb['neighbourhood'])
fig = plt.gcf()
fig.set_size_inches(25,6)
plt.title('Neighbourhood')


# In[24]:


#checking the type of room's


# In[38]:



sns.countplot(airbnb['room_type'], palette="plasma")
fig = plt.gcf()
fig.set_size_inches(10,10)
plt.title('Room type')


# In[27]:


# checking  relation between Neighbouring groups and Availability of room's 


# ### Brookiyn has the more number  of availability as compaired to others groups 

# In[28]:


plt.figure(figsize=(10,10))
ax = sns.boxplot(data=airbnb, x='neighbourhood_group',y='availability_365')


# ### ploting scatter plot to checking the distribution of Neighbourhood group

# In[30]:


plt.figure(figsize=(10,6))
sns.scatterplot(airbnb.longitude,airbnb.latitude,hue=airbnb.neighbourhood_group)
plt.ioff()


# In[40]:


# Neighbourhood


# In[31]:


plt.figure(figsize=(10,6))
sns.scatterplot(airbnb.longitude,airbnb.latitude,hue=airbnb.neighbourhood)
plt.ioff()


# In[34]:


#checking the Room type  wrt latitude and longitude 
plt.figure(figsize=(10,6))
sns.scatterplot(airbnb.longitude,airbnb.latitude,hue=airbnb.room_type)
plt.ioff()


# In[41]:


#Availability of Room 365 days  or across the whole year


# In[36]:


plt.figure(figsize=(10,6))
sns.scatterplot(airbnb.longitude,airbnb.latitude,hue=airbnb.availability_365)
plt.ioff()


# In[ ]:




