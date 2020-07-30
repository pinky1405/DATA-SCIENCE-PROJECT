#!/usr/bin/env python
# coding: utf-8

# In[2]:


# importing important libraries
import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
import pandas as pd
import seaborn as sns
from matplotlib.pyplot import figure, show


# In[3]:


#reading the csv file or dataset
file = pd.read_csv(sys.argv[1], error_bad_lines=False);


# In[4]:


#dropping all columns where all entries are  missing values 
file.dropna(axis=1, how='all',inplace=True)


# In[5]:


file.head()


# In[5]:


with PdfPages('visualization-output.pdf') as output_pdf:
    
    
     
    #2a. The number of students applied to different technologies. 
    file['Areas of interest'].value_counts().plot(kind='bar')
    plt.title('No of students who applied for different technologies')
    plt.ylabel('No of students')
    plt.xlabel('Technologies')
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    
    
    #2b. The number of students applied for Data Science who knew ‘’Python” and who didn’t. 
    df1=file[file['Areas of interest']=='Data Science ']
    import seaborn as sns 
    sns.countplot(df1['Programming Language Known other than Java (one major)']=='Python')
    plt.title('The number of students applied for Data Science who knew ‘’Python” and who didn’t')
    plt.xlabel("Python language known")
    plt.ylabel("Student in Data Science")
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    
    #2c. The different ways students learned about this program. 

    file['How Did You Hear About This Internship?'].value_counts().plot(kind='bar')
    plt.title('The different ways students learned about this program')
    plt.xlabel("The Different Ways")
    plt.ylabel("No of Student")
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    #2d. Students who are in the fourth year and have a CGPA greater than 8.0. 
    df2=file[file['Which-year are you studying in?']=='Fourth-year']
    sns.countplot(df2['CGPA/ percentage']>=8.0)
    plt.title('Student in fourth year having CGPA greater than 8')
    plt.xlabel("CGPA/Percentage greater than 8")
    plt.ylabel("Student in Fourth Year")
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    
    
    #2e.Students who applied for Digital Marketing with verbal and written communication score greater than 8. 
    df3 = file.loc[(file['Areas of interest'] == 'Digital Marketing ') &
              (file['Rate your verbal communication skills [1-10]'] > 8) &
              (file['Rate your written communication skills [1-10]'] > 8)]

    fig,ax = plt.subplots(figsize = (15,7))
    ax.set_ylabel('Number of Students')
    ax.set_xlabel('pointer rating')

    comm_counts = df3['Rate your written communication skills [1-10]'].value_counts()
    verbal_counts = df3['Rate your verbal communication skills [1-10]'].value_counts()
    sns.lineplot(x= comm_counts.index, y = comm_counts.values,ax = ax,label = 'Written Communication rating')
    sns.lineplot(x = verbal_counts.index, y = verbal_counts.values,ax =ax,label  = 'Verbal communication rating')
    plt.title("Students who applied for Digital Marketing with verbal and written communication score greater than 8")
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    #2f.Year-wise and area of study wise classification of students
    df5 = file[['Which-year are you studying in?', 'Major/Area of Study']]
    fig,ax = plt.subplots(figsize = (20,10))
    df5.groupby(['Major/Area of Study', 'Which-year are you studying in?'])       ['Which-year are you studying in?'].value_counts().unstack(0).plot.barh(ax=ax,rot = 0)

    plt.title(' Year-wise and area of study wise classification of students')
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    #2g.City and college wise classification of students. 
    df6=file[['City','College name']]
    fig,ax = plt.subplots(figsize = (25,15))
    df6.groupby(['City', 'College name'])       ['College name'].value_counts().unstack(0).plot.bar(ax=ax)
    plt.title('City and college wise classification of students. ')
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    
    
    #2h.Plot the relationship between the CGPA and the target variable. 
    sns.stripplot(x="Label", y="CGPA/ percentage",hue="Label",data=file)
    plt.title(' CGPA and the target variable')
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    ##2i.Plot the relationship between the Area of Interest and the target variable.
    major_df1=file.groupby(['Areas of interest','Label'])['Areas of interest'].size()[lambda x: x < 1000]
    fig,ax = plt.subplots(figsize = (15,7) )
    major_df1 = major_df1.to_frame()
    major_df1.unstack().plot.bar(ax =ax)
    plt.title("Area of Interest and the target variable ")
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    #2j.Plot the relationship between the year of study, major, and the target variable
    major_df=file.groupby(['Major/Area of Study','Which-year are you studying in?','Label'])['Major/Area of Study'].size()[lambda x: x < 1000]
    fig,ax = plt.subplots(figsize = (15,7) )
    major_df = major_df.to_frame()
    major_df.unstack().plot.bar(ax =ax)
    plt.title(" year of study, major and the target variable")
    output_pdf.savefig(bbox_inches="tight",pad_inches=2)
    plt.close()
    
    
    
    
    
    
   


# In[ ]:




