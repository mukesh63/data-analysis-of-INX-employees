#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


emp = pd.read_excel('C:/Users/ADMIN/Employee Project/Data/INX_Future_Inc_Employee_Performance_CDS_Project2_Data_V1.8.xls')


# In[3]:


emp


# In[4]:


emp.describe()


# In[5]:


emp.hist(bins=12, color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=12, ylabelsize=12, grid=False)    
plt.tight_layout(rect=(0, 0,2.5, 2.5))


# In[6]:


emp.info()


# In[7]:


emp.shape


# In[8]:


emp.columns


# In[9]:


emp.hist(bins=15, color='steelblue', edgecolor='black', linewidth=1.0,
           xlabelsize=12, ylabelsize=12, grid=False)    
plt.tight_layout(rect=(0, 0, 2.5, 2.5))


# In[10]:


#as we can ND of sample and population matches so our sample taken is in ND
emp['Age'].hist()


# In[11]:


emp['Age'].hist()


# In[12]:


emp['Age'].describe()


# In[13]:


emp.describe()


# In[14]:


emp1 = emp[emp['PerformanceRating']==2]
print(emp1.shape)


# In[15]:


emp1['PerformanceRating'].value_counts()


# In[16]:


sns.countplot(emp1['PerformanceRating'])


# In[17]:


emp['Age'].value_counts()


# In[18]:


sns.boxplot(emp1['Age'])


# In[19]:


sns.countplot(emp1['Age'])
sns.set(rc={'figure.figsize':(8.7,12.27)})


# In[20]:


emp1['Gender'].value_counts()


# In[21]:


sns.countplot(emp1['Gender'])
sns.set(rc={'figure.figsize':(5,5.27)})


# In[22]:


emp1['EducationBackground'].value_counts()


# In[23]:


sns.countplot(emp1['EducationBackground'])
sns.set(rc={'figure.figsize':(8,5.27)})


# In[24]:


emp1['MaritalStatus'].value_counts()


# In[25]:


sns.countplot(emp1['MaritalStatus'])


# In[26]:


emp1['EmpDepartment'].value_counts()


# In[27]:


sns.countplot(emp1['EmpDepartment'])
sns.set(rc={'figure.figsize':(12,5.27)})


# In[28]:


emp1['EmpJobRole'].value_counts()


# In[29]:


sns.countplot(emp1['EmpJobRole'])
sns.set(rc={'figure.figsize':(35,12.27)})


# In[30]:


import plotly.express as px

fig = px.pie(emp1, values='', names='', title='no of employee performing at 2')
fig.show()


# In[31]:


emp1['BusinessTravelFrequency'].value_counts()


# In[32]:


sns.countplot(emp1['BusinessTravelFrequency'])
sns.set(rc={'figure.figsize':(5,5.27)})


# In[33]:


emp1['DistanceFromHome'].value_counts()


# In[34]:


sns.countplot(emp1['DistanceFromHome'])


# In[35]:


sns.boxplot(emp1['DistanceFromHome'])


# In[36]:


emp1['EmpEducationLevel'].value_counts()


# In[37]:


sns.countplot(emp1['EmpEducationLevel'])


# In[38]:


emp1['EmpEnvironmentSatisfaction'].value_counts()


# In[39]:


sns.countplot(emp1['EmpEnvironmentSatisfaction'])


# In[40]:


emp1['EmpJobInvolvement'].value_counts()


# In[41]:


sns.countplot(emp1['EmpJobInvolvement'])


# In[42]:


emp1['EmpJobLevel'].value_counts()


# In[43]:


sns.countplot(emp1['EmpJobLevel'])


# In[44]:


emp1['EmpJobSatisfaction'].value_counts()


# In[45]:


sns.countplot(emp1['EmpJobSatisfaction'])


# In[46]:


emp1['NumCompaniesWorked'].value_counts()


# In[47]:


sns.countplot(emp1['NumCompaniesWorked'])


# In[48]:


sns.countplot(emp1['EmpJobSatisfaction'])


# In[49]:


emp1['OverTime'].value_counts()


# In[50]:


sns.countplot(emp1['OverTime'])


# In[51]:


emp1['EmpLastSalaryHikePercent'].value_counts()


# In[52]:


sns.boxplot(emp1['EmpLastSalaryHikePercent'])


# In[53]:


sns.countplot(emp1['EmpLastSalaryHikePercent'])


# In[54]:


emp1['EmpRelationshipSatisfaction'].value_counts()


# In[55]:


sns.countplot(emp1['EmpRelationshipSatisfaction'])


# In[56]:


emp['TotalWorkExperienceInYears'].value_counts()


# In[57]:


sns.boxplot(emp1['TotalWorkExperienceInYears'])


# In[58]:


emp1['TrainingTimesLastYear'].value_counts()


# In[59]:


sns.countplot(emp1['TrainingTimesLastYear'])


# In[60]:


emp1['EmpWorkLifeBalance'].value_counts()


# In[61]:


sns.countplot(emp1['EmpWorkLifeBalance'])


# In[62]:


emp['ExperienceYearsAtThisCompany'].value_counts()


# In[63]:


sns.boxplot(emp1['ExperienceYearsAtThisCompany'])


# In[64]:


emp1['ExperienceYearsInCurrentRole'].value_counts()


# In[65]:


sns.boxplot(emp1['ExperienceYearsInCurrentRole'])


# In[66]:


emp1['YearsSinceLastPromotion'].value_counts()


# In[67]:


sns.countplot(emp1['YearsSinceLastPromotion'])


# In[68]:


emp1['YearsWithCurrManager'].value_counts()


# In[69]:


sns.countplot(emp1['YearsWithCurrManager'])


# In[70]:


sns.boxplot(emp1['YearsWithCurrManager'])


# In[71]:


sns.boxplot(emp1['YearsSinceLastPromotion'])


# In[72]:


emp1['Attrition'].value_counts()


# In[73]:


sns.countplot(emp1['Attrition'])


# In[ ]:





# In[74]:


emp.pivot_table(values=['Age'], index=['PerformanceRating'],aggfunc = np.mean)
#young age group of people are performing well 


# In[75]:


emp.groupby(emp1.PerformanceRating).mean()


# In[76]:


emp1.loc[:, ['Age', 'PerformanceRating']]


# In[77]:


sns.barplot(x='MaritalStatus',y='Age',data=emp1)
sns.set(rc={'figure.figsize':(5.7,4.27)})


# In[78]:


emp1.pivot_table(values=['ExperienceYearsAtThisCompany'],
                       index=['Gender'],aggfunc = np.mean)


# In[79]:


sns.countplot(emp1['ExperienceYearsAtThisCompany'],hue=emp1['Gender'])
#in rating 2 womens are performing more 
#in rating 3 male are performing more
#in rating 4 both are almost equall
sns.set(rc={'figure.figsize':(9.7,4.27)})


# In[80]:


emp1.pivot_table(values=['PerformanceRating'],
                       index=['EducationBackground'],aggfunc = np.mean)
#overall marketing team is not performing well compare to others
sns.countplot


# In[81]:


sns.countplot(emp1['EmpRelationshipSatisfaction'],hue=emp1['MaritalStatus'])
sns.set(rc={'figure.figsize':(4,5.27)})


# In[82]:


emp1.pivot_table(values=['EmpRelationshipSatisfaction'],
                       index=['MaritalStatus'],aggfunc = np.mean)
#as we can see their is slight performnce difference between married and single status 


# In[ ]:





# In[83]:


a =emp1.pivot_table(values=['ExperienceYearsInCurrentRole'],
                       index=['EmpJobRole'],aggfunc = np.mean)
a


# In[84]:


sns.barplot(x='ExperienceYearsInCurrentRole',y='EmpJobRole',data= emp1)


# In[85]:


emp1.pivot_table(values=['EmpJobSatisfaction'],
                       index=['BusinessTravelFrequency'],aggfunc = np.mean)


# In[86]:


sns.countplot(x="EmpJobSatisfaction", hue="BusinessTravelFrequency", data= emp)


# In[87]:


emp1.pivot_table(values=['DistanceFromHome'],
                       index=['EmpDepartment'],aggfunc = np.mean)


# In[88]:


sns.barplot(x="EmpDepartment", y="DistanceFromHome", data= emp1)
sns.set(rc={'figure.figsize':(12,5.27)})


# In[89]:


emp1.pivot_table(values=['EmpJobInvolvement'],
                       index=['EmpJobRole'],aggfunc = np.mean)


# In[90]:


sns.barplot(x="EmpJobInvolvement", y="EmpJobRole", data= emp1)


# In[91]:


emp1.pivot_table(values=['YearsWithCurrManager'],
                       index=['EmpJobRole'],aggfunc = np.mean)


# In[145]:


sns.barplot(x="YearsWithCurrManager", y="EmpJobRole", data= emp1)


# In[141]:


emp1.pivot_table(values=['YearsSinceLastPromotion'],
                       index=['EmpDepartment'],aggfunc = np.mean)


# In[143]:


sns.barplot(x='YearsSinceLastPromotion', y='EmpDepartment', data= emp1)


# In[144]:


emp1.pivot_table(values=['TrainingTimesLastYear'],
                       index=['EmpJobRole'],aggfunc = np.mean)


# In[173]:


sns.catplot(data = emp1, x="TrainingTimesLastYear", y="EmpJobRole", hue='Gender', kind='bar',
            height =7,)
plt.show()


# # Multi var analysis
# 

# In[180]:


d=emp1.pivot_table(values=['ExperienceYearsAtThisCompany','YearsSinceLastPromotion','ExperienceYearsInCurrentRole','YearsWithCurrManager'],
                       index=['EmpDepartment','EmpJobRole','MaritalStatus'],aggfunc = np.mean)
d
#human resouces not working perfecctly adn even sales dept is slow 
#Research & Development dep Senior Manager R&D even working low


# In[181]:


sns.pairplot(d)


# In[121]:


g =emp1.pivot_table(values=['EmpWorkLifeBalance','EmpLastSalaryHikePercent','PerformanceRating'],
                       index=['EmpDepartment','EmpJobRole'],aggfunc = np.mean)
g
g.sort_values(by='PerformanceRating')


# In[122]:


emp1['EmpLastSalaryHikePercent'].mode()


# In[123]:


import plotly.express as px
fig = px.sunburst(emp, path=['PerformanceRating', 'EmpDepartment', 'EmpJobRole','BusinessTravelFrequency'])
fig.show()


# In[124]:


emp1 = emp[emp['PerformanceRating']==2]
print(emp1.shape)


# In[125]:


emp1.info()


# In[126]:


import plotly.express as px
fig = px.sunburst(emp1, path=['PerformanceRating', 'EmpDepartment', 'EmpJobRole','Gender','MaritalStatus'])
fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[127]:


h = emp1.pivot_table(values=['YearsWithCurrManager','YearsSinceLastPromotion'],
                       index=['EmpDepartment','EmpJobRole'],aggfunc = np.mean)
h


# In[128]:


sns.pairplot(h)


# In[129]:


emp1.pivot_table(values=['YearsWithCurrManager','YearsSinceLastPromotion','PerformanceRating','EmpHourlyRate'],
                       index=['EmpDepartment','EmpJobRole','OverTime'],aggfunc = np.mean)


# In[130]:


emp1.pivot_table(values=['YearsWithCurrManager','PerformanceRating'],
                       index=['EmpDepartment','EmpJobRole','OverTime'],aggfunc = np.mean)


# In[131]:


f=emp1.corr()
f


# In[133]:


emp1.pivot_table(values=['EmpJobLevel','TotalWorkExperienceInYears','DistanceFromHome'],
                 index=['EmpDepartment','EmpJobRole','Gender',])


# In[134]:


import plotly.express as px
fig = px.sunburst(emp1, path=['PerformanceRating','EmpWorkLifeBalance','EmpDepartment', 'EmpJobRole'])
fig.show()
import plotly.express as px
fig = px.sunburst(emp1, path=['PerformanceRating', 'EmpDepartment', 'EmpJobRole','Gender','MaritalStatus'])
fig.show()
import plotly.express as px
fig = px.sunburst(emp1, path=['PerformanceRating','EmpEnvironmentSatisfaction','EmpDepartment', 'EmpJobRole'])
fig.show()


# In[135]:


import plotly.express as px
fig = px.sunburst(emp1, path=['PerformanceRating','EmpJobInvolvement','EmpDepartment', 'EmpJobRole','Gender'])
fig.show()


# In[136]:


emp1.pivot_table(values=['EmpEnvironmentSatisfaction','EmpJobInvolvement','EmpJobSatisfaction','EmpRelationshipSatisfaction','EmpWorkLifeBalance','EmpJobLevel'],
                 index=['EmpDepartment','EmpJobRole',])


# In[137]:


import plotly.express as px
fig = px.sunburst(emp1, path=['EmpJobSatisfaction','EmpDepartment', 'EmpJobRole','Gender'])
fig.show()


# In[138]:


fig = px.scatter(emp1,x = 'EmpWorkLifeBalance',y='EmpJobRole',color ='Gender',
                title='Work life Balance')
fig.show()


# In[139]:


emp1.pivot_table(values=['YearsWithCurrManager','ExperienceYearsAtThisCompany','EmpLastSalaryHikePercent'],
                 index=['EmpJobInvolvement','EmpDepartment','EmpJobRole'])


# In[140]:


emp1.pivot_table(values=['EmpJobLevel','TrainingTimesLastYear',],
                 index=['EmpDepartment','EmpJobRole','Gender'])


# In[182]:


f, ax = plt.subplots(figsize=(15, 9))
corr = emp1.corr()
hm = sns.heatmap(corr, annot=True, ax=ax, cmap="coolwarm",
                 linewidths=.05)
f.subplots_adjust(top=0.93)
t= f.suptitle('EMPLOYESS ATTRIBUTE CORRELATION HEATMAP', fontsize=14)


# In[ ]:





# In[ ]:





# In[ ]:




