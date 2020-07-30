#!/usr/bin/env python
# coding: utf-8

# In[2]:


#importing the libraries
import os
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')


# In[7]:


#reading the csv file or dataset
file = pd.read_csv(sys.argv[1], error_bad_lines=False);


# In[8]:


file.drop(['First Name','Last Name','Email Address','DOB [DD/MM/YYYY]','Zip Code','Contact Number','Emergency Contact Number','State'],axis=1,inplace=True)


# In[9]:


#dropping all columns where all entries are  missing values 
file.dropna(axis=1, how='all',inplace=True)


# In[10]:


from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()
le.fit_transform(['ineligible','eligible'])
file['Label'] = file['Label'].map({'ineligible': 0,'eligible': 1})


# In[11]:


le=LabelEncoder()
le.fit_transform(['No','Yes'])
file['Have you worked core Java'] = file['Have you worked core Java'].map({'No': 0,'Yes': 1})


# In[12]:


le=LabelEncoder()
le.fit_transform(['No','Yes'])
file['Have you worked on MySQL or Oracle database'] = file['Have you worked on MySQL or Oracle database'].map({'No': 0,'Yes': 1})


# In[13]:


le=LabelEncoder()
le.fit_transform(['No','Yes'])
file['Have you studied OOP Concepts'] = file['Have you studied OOP Concepts'].map({'No': 0,'Yes': 1})


# In[14]:


# create a list pf feature to dummy
todummy_list = ['City','Gender','College name','University Name','Degree','Major/Area of Study','Course Type','Which-year are you studying in?','Areas of interest','Current Employment Status','Programming Language Known other than Java (one major)','How Did You Hear About This Internship?']


# In[15]:


#fuction to dummy all
def dummy_df(df, todummy_list):
    for x in todummy_list:
        dummies= pd.get_dummies(df[x], prefix=x ,dummy_na=False)
        df=df.drop(x,1)
        df=pd.concat([df,dummies], axis=1)
    return df 


# In[16]:


file=dummy_df(file,todummy_list)
file.head()


# # RANDOM FOREST CLASSIFIER

# In[23]:




#seperating independent and dependent variables
x = file.drop(['Label'], axis=1)
y = file['Label']
x.shape, y.shape


# In[34]:


# Importing the train test split function
from sklearn.model_selection import train_test_split
train_x,test_x,train_y,test_y = train_test_split(x,y, test_size=0.3)


# In[35]:


## Importing the MinMax Scaler
from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
x_scaled = scaler.fit_transform(x)


# In[36]:


x = pd.DataFrame(x_scaled, columns = x.columns)


# In[37]:


#Import Random Forest Model
from sklearn.ensemble import RandomForestClassifier

#Create a Gaussian Classifier
clf=RandomForestClassifier(n_estimators=100)

#Train the model using the training sets y_pred=clf.predict(X_test)
clf.fit(train_x,train_y)

y_pred=clf.predict(test_x)


# In[38]:


from sklearn.metrics import f1_score
# Calculating f1-score
k = f1_score(y_pred, test_y)
print('Calculating f1_score', k )


# In[ ]:




