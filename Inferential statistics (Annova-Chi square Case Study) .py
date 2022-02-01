#!/usr/bin/env python
# coding: utf-8

# # ANOVA and Chi Square 

# ### Practice Exercise 1 (10 marks)

# A company makes three types of electronic device.
# Life time in hours for each type of electronic device is given below:
# 
# * life_type_A = [ 407, 411, 409 ]
# * life_type_B = [ 404, 406, 408, 405, 402 ]
# * ife_type_C  = [ 410, 408, 406, 408]

# ### import libraries

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as st
import statsmodels.stats as smt


# In[2]:


life_type_A=np.array( [ 407, 411, 409 ])
life_type_B=np.array( [ 404, 406, 408, 405, 402 ])
life_type_C=np.array([ 410, 408, 406, 408])


# ### a)  Write your inferene on the group means from the above boxplots.

# In[3]:


a=print('mean of A is ',life_type_A.mean())
b=print('mean of B is ',life_type_B.mean())
c=print('mean of C is ',life_type_C.mean())


# In[6]:


df=pd.DataFrame()

df1=pd.DataFrame({"Group":"A","life_type":life_type_A})
df2=pd.DataFrame({"Group":"B","life_type":life_type_B})
df3=pd.DataFrame({"Group":"C","life_type":life_type_C})

df =df.append(df1) 
df =df.append(df2) 
df =df.append(df3)


# In[7]:


sns.boxplot(x='Group',y='life_type',data=df)
plt.title('group means')
plt.show()


# ### b)  At 5% level of significance, is there any difference in the average lifetimes of the three types?

# In[8]:


st.f_oneway(life_type_A ,life_type_B,life_type_C)


# In[ ]:





# ## Chi Square

# ##### Practice Exercise 2 (5 Marks)
Refer to the above example 5. Here the operations manager changes his belief and now believes that 28% of their passengers prefer vegan food, 42% prefer vegetarian food , 25% prefer non-veg food 5% request for Jain food. 

At 5% level of significance, can you confirm that the meal preference is as per the belief of the operations manager?
# In[11]:


import scipy.stats as stats
import scipy

observed_values    = scipy.array([190, 185, 90, 35])
n                  = observed_values.sum()


# In[12]:


expected_values    = scipy.array([n*.28, n*.42, n*.25, n*.05])
stats.chisquare(observed_values,expected_values)


# ### Chi-square tests of independence

# ### Practice Exercise 3 (5 marks)

# A Cable service provider company is interested in checking whether or not the customer churn depends on customer segment.  Use 5% as level of significance

# | Customer Segment | Churned | Retained |
# |  -------- | ----- | ---- |
# | S1 | 15 | 142 |
# | S2 | 24 | 400 |
# | S3 | 30 | 389 |
# 

# #### Hint

# In[13]:


import numpy       as np
import scipy.stats as stats

churn_array = np.array([[15,142],[24, 400],[30, 389]])
stats.chi2_contingency(churn_array)


# In[14]:


from scipy import stats

print('Chi-square statistic %3.5f P value %1.6f Degrees of freedom %d' %(stats.chi2_contingency(churn_array)[0:3]))


# ## E N D  
