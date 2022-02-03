#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page = requests.get('https://www.imdb.com/chart/top/')
page


# In[3]:


soup = BeautifulSoup(page.content, "html.parser")
soup


# In[4]:


name = soup.find_all("h3", class_="lister-item-header")

# get text from movie name web elements

movies_name = [] #empty list

for i in name:

    for j in i.find_all("a"):

        movies_name.append(j.text)


# In[10]:


name=soup.find_all(class_="titleColumn")


# name

# In[11]:


name


# In[12]:


movies_name = [] #empty list

for i in name:

    for j in i.find_all("a"):

        movies_name.append(j.text)


# In[13]:


movies_name


# In[48]:


year =soup.find('span',class_="secondaryInfo")
year


# In[51]:


year.text.split()


# In[52]:


movies_name


# In[54]:


rating= soup.find("td",class_="ratingColumn imdbRating")
rating


# In[55]:


rating.text.split()


# In[59]:


movies_rating = []
for i in soup.find_all("td",class_="ratingColumn imdbRating"):
    movies_rating.append(i.text)
    
movies_rating


# In[60]:


movies_year= []
for i in soup.find_all('span',class_="secondaryInfo"):
    movies_year.append(i.text)
    
movies_year


# In[64]:


print(len(movies_name),len(movies_year),len(movies_rating))


# In[62]:


# making DataFrame


# In[63]:


import pandas as pd


# In[67]:


df = pd.DataFrame({"movies_name":movies_name,"movies_year":movies_year,"movies_rating":movies_rating})
df


# In[68]:


df


# In[ ]:




