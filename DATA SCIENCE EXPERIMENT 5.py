#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt
marks=[13,45,63,78] 
student=['ABC','QOR','EFB','TOB'] 
plt.plot(marks,student) 
plt.xlabel('Marks') 
plt.ylabel('Student name') 
plt.show()


# In[2]:


student=['A','B','C','D'] 
attendence=[90,85,73,88] 
plt.plot(attendence,student) 
plt.xlabel('Attendence') 
plt.ylabel('Student name') 
plt.show()


# In[3]:


x=[10,20,30,40,50] 
y=[100,200,300,400,500] 
plt.scatter(x,y,label='stars',color='green',marker='*',s=30) 
plt.show()


# In[4]:


x=np.arange(0,15) 
y=np.arange(0,15) 
x 
y 
plt.scatter(x,y,c='r') 
plt.xlabel('X axis') 
plt.ylabel('y axis') 
plt.title('Scatter plot') 
plt.show()


# In[5]:


act=['eat','sleep','work','play'] 
slices=[3,7,8,6] 
color=['r','y','g','b'] 
plt.pie(slices,labels=act,colors=color,startangle=90,shadow=True,explode=(0.1,0.1,0.1,0.1),radius=1.2,autopct='%1.1f%%') 
plt.legend() 
plt.show()


# In[6]:


feedback=['Good','excellent','Perfect','Ok'] 
slices=[4,10,3,8] 
color=['y','r','b','g'] 
plt.pie(slices,labels=feedback,colors=color,startangle=90,shadow=True,explode=(0.1,0.1,0.1,0.1),radius=1.2,autopct='%1.1f%%') 
plt.legend() 
plt.show()


# In[7]:


x = [1, 2, 3, 4, 5] 
y1 = [10, 12, 14, 16, 18] 
y2 = [5, 7, 9, 11, 13]
plt.fill_between(x, y1, color='blue') 
plt.fill_between(x, y2, color='green') 
plt.plot(x, y1, color='red') 
plt.plot(x, y2, color='black') 
plt.legend(['y1','y2']) 
plt.show()


# In[8]:


height = [10, 24, 36, 40, 5] 
names = ['one', 'two', 'three', 'four', 'five'] 
c1=['red', 'green'] 
c2=['b', 'g'] 
plt.bar (names, height, width=0.8, color=c1) 
plt.xlabel('x - axis') 
plt.ylabel('y - axis') 
plt.title('My bar chart!') 
plt.show()


# In[9]:


x = [2,1,6,4,2,4,8,9,4,2,4,10,6,4,5,7,7,3,2,7,5,3,5,9,2,1] 
plt.hist(x, bins = 10, color='blue', alpha=0.5) 
plt.show()


# In[10]:


np.random.seed(0) 
data=np.random.normal(loc=0, scale=1, size=100) 
data


# In[11]:


fig, ax= plt.subplots() 
ax.boxplot(data) 
ax.set_xlabel('Data') 
ax.set_ylabel('Values') 
ax.set_title('Box Plot')


# In[ ]:




