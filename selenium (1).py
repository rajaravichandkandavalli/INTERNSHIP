#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


import selenium
from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[3]:


driver = webdriver.Chrome('chromedriver.exe')


# In[4]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[5]:


# finding web element for search job bar using class name

search_job = driver.find_element_by_class_name("suggestor-input")
search_job


# In[6]:


search_job.send_keys('data scientist')


# In[7]:


search_loc = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_loc


# In[8]:


search_loc.send_keys('Hyderabad')


# In[9]:


search_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn


# In[10]:


search_btn.click()


# # cliking filtres by selecting check boxes using absolute  xpath

# In[11]:


salary_check = driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/section[1]/div[2]/div[4]/div[2]/div[1]/label/i')


# In[12]:


salary_check.click()


# lets create a empty 4 lists

# # Extracting job titles

# In[13]:


title_tags = driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(title_tags)


# In[14]:


# now the text of job title is inside the web elements extracted above
# so we will run a for loop to iterate over the tags and will extract text from them

job_titles = []

for i in title_tags:
    job_titles.append(i.text)
    
len(job_titles)


# In[15]:


job_titles


# # Extracting company names

# In[19]:


company_tags = driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
len(company_tags)


# In[20]:


company_titles = []

for i in company_tags:
    company_titles.append(i.text)
    
len(company_titles)


# In[21]:


company_titles


# # extracting experience

# In[22]:


exp_tags = driver.find_elements_by_xpath('//span[contains(@title,"Yrs")]')
len(exp_tags)


# In[23]:


experience=[]

for i in exp_tags:
    experience.append(i.text)
len(experience)


# In[24]:


experience


# # Extracting location

# In[25]:


locn_tags = driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(locn_tags)


# In[26]:


location =[]
for i in locn_tags:
    location.append(i.text)
len(location)


# In[27]:


location


# # Extracting salary

# In[28]:


sal_tags = driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi salary"]')
len(sal_tags)


# In[29]:


salary=[]
for i in sal_tags:
    salary.append(i.text)
len(salary)


# In[30]:


salary


# In[31]:


len(job_titles),len(company_titles),len(experience),len(location),len(salary)


# In[33]:


jobs = pd.DataFrame()
jobs['Job Title']= job_titles
jobs['Company']= company_titles

jobs['Location']= location
jobs['Salary']= salary
jobs


# In[1]:


import selenium


# In[2]:


from selenium import webdriver
import pandas as pd
import warnings
warnings.filterwarnings('ignore')


# In[3]:


driver = webdriver.Chrome('chromedriver.exe')


# In[4]:


url = 'https://www.naukri.com/'
driver.get(url)


# In[5]:


search_job = driver.find_element_by_class_name("suggestor-input")
search_job


# In[7]:


search_job.send_keys('data scientist')


# In[8]:


search_loc = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[3]/div/div/div/input')
search_loc


# In[9]:


search_loc.send_keys('delhi')


# In[10]:


search_btn = driver.find_element_by_xpath('/html/body/div/div[2]/div[3]/div/div/div[6]')
search_btn


# In[11]:


search_btn.click()


# In[12]:


title_tags = driver.find_elements_by_xpath('//a[@class="title fw500 ellipsis"]')
len(title_tags)


# In[14]:


job_titles = []

for i in title_tags:
    job_titles.append(i.text)
    
len(job_titles)


# In[15]:


job_titles


# In[16]:


company_tags = driver.find_elements_by_xpath('//a[@class="subTitle ellipsis fleft"]')
len(company_tags)


# In[17]:


company_titles = []

for i in company_tags:
    company_titles.append(i.text)
    
len(company_titles)


# In[18]:


company_titles


# In[19]:


exp_tags = driver.find_elements_by_xpath('//span[contains(@title,"Yrs")]')
len(exp_tags)


# In[20]:


experience=[]

for i in exp_tags:
    experience.append(i.text)
len(experience)


# In[21]:


experience


# In[22]:


locn_tags = driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi location"]')
len(locn_tags)


# In[23]:


location =[]
for i in locn_tags:
    location.append(i.text)
len(location)


# In[24]:


location


# In[25]:


sal_tags = driver.find_elements_by_xpath('//li[@class="fleft grey-text br2 placeHolderLi salary"]')
len(sal_tags)


# In[26]:


salary=[]
for i in sal_tags:
    salary.append(i.text)
len(salary)


# In[27]:


salary


# In[28]:


len(job_titles),len(company_titles),len(experience),len(location),len(salary)


# In[29]:


jobs = pd.DataFrame()
jobs['Job Title']= job_titles
jobs['Company']= company_titles
jobs['Experience']= experience
jobs['Location']= location
jobs['Salary']= salary
jobs


# In[ ]:




