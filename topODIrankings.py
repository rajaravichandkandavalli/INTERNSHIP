#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[4]:


page= requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/test')
page


# In[5]:


soup = BeautifulSoup(page.content, "html.parser")
soup


# In[8]:


name=soup.find(class_="rankings-block__container full rankings-table")
name


# In[9]:


name.text.split()


# In[10]:


name = soup.find(class_="rankings-block__banner--team-name")
name


# In[11]:


name.text.split()


# In[12]:


name=soup.find_all(class_="rankings-block__banner--team-name")
name


# In[18]:


name.text.split()
len(name)


# In[15]:


name= soup.find(class_="rankings-block__container full rankings-table")
name


# In[16]:


name.text.split()


# In[19]:


name


# In[20]:


name = soup.find(class_="rankings-block__banner--team-name")
name


# In[21]:


name.text.split()


# In[23]:


for i in name:

    for j in i.find_all('span'):

        product_name.append(j.text)


# In[ ]:




