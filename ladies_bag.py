#!/usr/bin/env python
# coding: utf-8

# In[1]:


from bs4 import BeautifulSoup
import requests
import pandas as pd


# In[2]:


page = requests.get('https://meesho.com/bags-ladies/pl/p7vbp')
page


# In[3]:


soup = BeautifulSoup(page.content, "html.parser")
soup


# In[5]:


name=soup.find(class_="sc-dkPtRN ProductList__GridCol-sc-8lnc8o-0 FjWWx jMkQHN")
name


# In[6]:


name.text.split()


# In[7]:


name= soup.find(class_="sc-gsDKAQ Grid__Row-sc-4ki5nk-0 iQiJjX gfsqfL products")
name


# In[8]:


name.text.split()


# In[9]:


name=soup.find(class_="ProductListingContent__HeadLine1-sc-e96brm-0 hXLzGF")
name


# In[10]:


name.text.split()


# In[11]:


name= soup.find(class_="sc-bdvvtL ProductList__PLPContainer-sc-8lnc8o-1 byHcNc eVzmpH")
name


# In[12]:


name.text.split()


# In[13]:


len(name)


# In[14]:


name=soup.find(class_="sc-gsDKAQ Grid__Row-sc-4ki5nk-0 iQiJjX gfsqfL products")
name


# In[15]:


name.text.split()


# In[16]:


name=soup.find(class_="sc-bdvvtL Desktop__ContainerStyled-sc-1jz570n-0 byHcNc kfIzHc")
name


# In[17]:


name.text.split()


# In[18]:


name=soup.find(class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS")
name


# In[19]:


name.text.split()


# In[20]:


name=soup.find_all(class_="Text__StyledText-sc-oo0kvp-0 bWSOET NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4 cQhePS")
name


# In[28]:


product_name = [] #empty list

for i in name:

    for j in i.find_all("p"):

        product_name.append(j.text)


# In[29]:


product_name


# In[30]:


set(name)


# In[31]:


name.keys()


# In[ ]:




