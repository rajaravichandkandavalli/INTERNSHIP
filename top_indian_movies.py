#!/usr/bin/env python
# coding: utf-8

# In[7]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[8]:


page = requests.get('https://www.imdb.com/india/top-rated-indian-movies/')
page


# In[9]:


soup = BeautifulSoup(page.content, "html.parser")
soup


# In[10]:


name=soup.find(class_="titleColumn")


# In[11]:


name


# In[12]:


name.text.split()


# In[14]:


year=soup.find(class_="secondaryInfo")
year


# In[15]:


year.text.split()


# In[16]:


rating=soup.find(class_="ratingColumn imdbRating")
rating


# In[17]:


rating.text.split()


# In[19]:


name


# In[20]:


name.text.split()


# In[21]:


name=soup.find_all(class_="titleColumn")
name


# In[23]:


movies_name = [] #empty list

for i in name:

    for j in i.find_all("a"):

        movies_name.append(j.text)


# In[24]:


movies_name


# In[25]:


year=soup.find_all(class_="secondaryInfo")
year


# In[26]:


movies_year= []
for i in soup.find_all('span',class_="secondaryInfo"):
    movies_year.append(i.text)
    
movies_year


# In[27]:


rating=soup.find_all(class_="ratingColumn imdbRating")
rating


# In[28]:


movies_rating = []
for i in soup.find_all("td",class_="ratingColumn imdbRating"):
    movies_rating.append(i.text)
    
movies_rating


# In[29]:


df = pd.DataFrame({"movies_name":movies_name,"movies_year":movies_year,"movies_rating":movies_rating})
df


# In[30]:


df.info


# In[31]:


df.shape


# In[33]:


df.describe()


# In[36]:


df.


# In[38]:


df['movies_name']


# In[ ]:




