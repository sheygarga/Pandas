
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np


# In[3]:


schools_df = pd.read_csv('schools_complete.csv')
students_df = pd.read_csv('students_complete.csv')
students_df.head()


# In[4]:


schools_df.head()


# In[5]:


district_df = pd.DataFrame(columns=['Total Schools','Total Students','Total Budget','Avg Math Score','Avg Reading Score',
                                   '% Passing Math','% Passing Reading','% Overall Passing Rate'
                                  ],index = [0])
district_df


# In[16]:


district_df['Total Schools']= schools_df['name'].count()
district_df['Total Students'] = schools_df['size'].sum()
money = schools_df['budget'].sum()
district_df['Total Budget'] = '${:,.2f}'.format(money)
district_df['Avg Math Score'] = '%.2f' % students_df['math_score'].mean()
district_df['Avg Reading Score'] = '%.2f' % students_df['reading_score'].mean()
passing_math = students_df['math_score'][students_df['math_score']>60]
district_df['% Passing Math'] =  (passing_math.count()/(schools_df['size'].sum()))*100
passing_read = students_df['reading_score'][students_df['reading_score']>60]
district_df['% Passing Reading'] =  (passing_read.count()/(schools_df['size'].sum()))*100
district_df['% Overall Passing Rate'] = ((district_df['% Passing Reading'])+(district_df['% Passing Math']))/2
district_df


# In[20]:


#come back to this for percentages

schoolSum_df = pd.DataFrame(columns=['School Type','Total Students','Total School Budget','Per Student Budget',
                                   'Average Math Score','Average Reading Score','% Passing Math','% Passing Reading',
                                   '% Overall Passing Rate'])
#schoolSum_df['School Type'] = schoolSum_df.fillna(0)
#schoolSum_df['name'] = schools_df.ix[:,'type']
schoolSum_df['name'] = schools_df['name']
schoolSum_df = schoolSum_df.fillna(0)
schoolSum_df['School Type'] = schools_df.loc[:,'type']
students_df.groupby(by = 'school')
schoolSum_df['Total Students']=schoolSum_df['name'].map(students_df['school'].value_counts())
schoolSum_df['Total School Budget']=schools_df['budget']
schoolSum_df['Per Student Budget'] = schoolSum_df['Total School Budget']/schoolSum_df['Total Students']
schoolSum_df['Average Math Score'] = schoolSum_df['name'].map(students_df.groupby(['school'])['math_score'].mean())
schoolSum_df['Average Reading Score'] = schoolSum_df['name'].map(students_df.groupby(['school'])['reading_score'].mean())
students_df['math_score'] = students_df['math_score'].astype(np.int32)

i = 0
for name in schoolSum_df['name']:
    val = students_df[(students_df['school'] == name)]
    val1 = val['math_score'].astype(np.int32)
    val2 = val['reading_score'].astype(np.int32)
    val1 = val1.values
    val2 = val2.values
    total_stu = schoolSum_df.at[i, 'Total Students']
    passing_stu_math = val1[np.where(val1>60)].size
    passing_stu_read = val2[np.where(val2>60)].size
    
    #print(total_stu, passing_stu_math, passing_stu_read, len(val), len(val1),len(val2) )
    #print(type(val),type(val1),type(val2))
    math_val = (passing_stu_math/total_stu)*100
    read_val = (passing_stu_read/total_stu)*100
    schoolSum_df.at[i,'% Passing Math'] = math_val
    schoolSum_df.at[i,'% Passing Reading'] = read_val
    schoolSum_df.at[i, '% Overall Passing Rate'] = (math_val+read_val)/2
    i = i + 1
    


#temp_passing_count =students_df.groupby(['school'])(students_df['math_score']>60).count()

#math_perc = students_df.groupby(['school'])['math_score'>60]
#schoolSum_df['% Passing Math']
#schoolSum_df
#math_perc
#temp = pd.DataFrame(columns = ['schools','math score'])
#temp_array = students_df['math_score']
#temp_var = (temp_array>60).count()
#temp['math score'] = temp_var
schoolSum_df
#temp_passing_count
#students_df


# In[21]:


math_grade = pd.DataFrame(columns = ['name','9th','10th','11th','12th'])
math_grade['name'] = schools_df['name']
math_grade = math_grade.fillna(0)

i = 0
for name in math_grade['name']:
    val=students_df[(students_df['grade']=='9th') & (students_df['school']==name)]['math_score'].mean()
    math_grade.at[i,'9th'] = val
    i = i + 1
i = 0
for name in math_grade['name']:
    val=students_df[(students_df['grade']=='10th') & (students_df['school']==name)]['math_score'].mean()
    math_grade.at[i,'10th'] = val
    i = i + 1
i = 0
for name in math_grade['name']:
    val=students_df[(students_df['grade']=='11th') & (students_df['school']==name)]['math_score'].mean()
    math_grade.at[i,'11th'] = val
    i = i + 1
i = 0
for name in math_grade['name']:
    val=students_df[(students_df['grade']=='12th') & (students_df['school']==name)]['math_score'].mean()
    math_grade.at[i,'12th'] = val
    i = i + 1
math_grade


# In[22]:


read_grade = pd.DataFrame(columns = ['name','9th','10th','11th','12th'])
read_grade['name'] = schools_df['name']
read_grade = read_grade.fillna(0)

i = 0
for name in read_grade['name']:
    val=students_df[(students_df['grade']=='9th') & (students_df['school']==name)]['reading_score'].mean()
    read_grade.at[i,'9th'] = val
    i = i + 1
i = 0
for name in read_grade['name']:
    val=students_df[(students_df['grade']=='10th') & (students_df['school']==name)]['reading_score'].mean()
    read_grade.at[i,'10th'] = val
    i = i + 1
i = 0
for name in read_grade['name']:
    val=students_df[(students_df['grade']=='11th') & (students_df['school']==name)]['reading_score'].mean()
    read_grade.at[i,'11th'] = val
    i = i + 1
i = 0
for name in read_grade['name']:
    val=students_df[(students_df['grade']=='12th') & (students_df['school']==name)]['reading_score'].mean()
    read_grade.at[i,'12th'] = val
    i = i + 1
read_grade


# In[41]:


score_budget = pd.DataFrame(columns = ['Per Student Budget','Average Math Score','Average Reading Score','% Passing Math'
                                       ,'% Passing Reading','% Overall Passing Rate'])
budget_holder = schoolSum_df['Per Student Budget']
out = pd.cut(budget_holder, 4)
#budget_holder
#counts = pd.value_counts(out)
#score_budget['Per Student Budget'] = out[1]
#out
score_budget['Per Student Budget'] = ['577.923 - 597.25','597.25 - 616.5','616.5 - 635.75','635.75-655.0']

val=schoolSum_df[(schoolSum_df['Per Student Budget'].astype(np.int32) >= 577.923) & (schoolSum_df['Per Student Budget'].astype(np.int32) <=595.25)]
score_budget['Average Math Score'][0] = val['Average Math Score'].mean()
score_budget['Average Reading Score'][0] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_budget['% Passing Math'][0] = val['% Passing Math'].mean()
score_budget['% Passing Reading'][0] = val['% Passing Reading'].mean()
score_budget['% Overall Passing Rate'][0] = (score_budget['% Passing Math'][0] + score_budget['% Passing Reading'][0])/2
#print()

val=schoolSum_df[(schoolSum_df['Per Student Budget'].astype(np.int32) >= 597.25) & (schoolSum_df['Per Student Budget'].astype(np.int32) <=616.5)]
score_budget['Average Math Score'][1] = val['Average Math Score'].mean()
score_budget['Average Reading Score'][1] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_budget['% Passing Math'][1] = val['% Passing Math'].mean()
score_budget['% Passing Reading'][1] = val['% Passing Reading'].mean()
score_budget['% Overall Passing Rate'][1] = (score_budget['% Passing Math'][1] + score_budget['% Passing Reading'][1])/2

val=schoolSum_df[(schoolSum_df['Per Student Budget'].astype(np.int32) >= 616.5) & (schoolSum_df['Per Student Budget'].astype(np.int32) <=635.75)]
score_budget['Average Math Score'][2] = val['Average Math Score'].mean()
score_budget['Average Reading Score'][2] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_budget['% Passing Math'][2] = val['% Passing Math'].mean()
score_budget['% Passing Reading'][2] = val['% Passing Reading'].mean()
score_budget['% Overall Passing Rate'][2] = (score_budget['% Passing Math'][2] + score_budget['% Passing Reading'][2])/2

val=schoolSum_df[(schoolSum_df['Per Student Budget'].astype(np.int32) >= 635.75) & (schoolSum_df['Per Student Budget'].astype(np.int32) <=655.0)]
score_budget['Average Math Score'][3] = val['Average Math Score'].mean()
score_budget['Average Reading Score'][3] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_budget['% Passing Math'][3] = val['% Passing Math'].mean()
score_budget['% Passing Reading'][3] = val['% Passing Reading'].mean()
score_budget['% Overall Passing Rate'][3] = (score_budget['% Passing Math'][3] + score_budget['% Passing Reading'][3])/2
#val


score_budget


# In[42]:


score_size = pd.DataFrame(columns = ['School Size','Average Math Score','Average Reading Score','% Passing Math'
                                       ,'% Passing Reading','% Overall Passing Rate'])
size_holder = schoolSum_df['Total Students']
out = pd.cut(size_holder,3)
#out
score_size['School Size'] = ['Small (<1943)','Medium (1943-3459)','Large (>3459)']

val=schoolSum_df[(schoolSum_df['Total Students'].astype(np.int32) < 1944)]
score_size['Average Math Score'][0] = val['Average Math Score'].mean()
score_size['Average Reading Score'][0] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_size['% Passing Math'][0] = val['% Passing Math'].mean()
score_size['% Passing Reading'][0] = val['% Passing Reading'].mean()
score_size['% Overall Passing Rate'][0] = (score_size['% Passing Math'][0] + score_size['% Passing Reading'][0])/2

val=schoolSum_df[(schoolSum_df['Total Students'].astype(np.int32) >1943 ) & (schoolSum_df['Total Students'].astype(np.int32) <3460)]
score_size['Average Math Score'][1] = val['Average Math Score'].mean()
score_size['Average Reading Score'][1] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_size['% Passing Math'][1] = val['% Passing Math'].mean()
score_size['% Passing Reading'][1] = val['% Passing Reading'].mean()
score_size['% Overall Passing Rate'][1] = (score_size['% Passing Math'][1] + score_size['% Passing Reading'][1])/2

val=schoolSum_df[(schoolSum_df['Total Students'].astype(np.int32) > 3460)]
score_size['Average Math Score'][2] = val['Average Math Score'].mean()
score_size['Average Reading Score'][2] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_size['% Passing Math'][2] = val['% Passing Math'].mean()
score_size['% Passing Reading'][2] = val['% Passing Reading'].mean()
score_size['% Overall Passing Rate'][2] = (score_size['% Passing Math'][2] + score_size['% Passing Reading'][2])/2

#val
score_size


# In[43]:


score_type =  pd.DataFrame(columns = ['School Type','Average Math Score','Average Reading Score','% Passing Math'
                                       ,'% Passing Reading','% Overall Passing Rate'])
score_type['School Type'] = ['Charter','District']

val = schoolSum_df[(schoolSum_df['School Type'] == 'Charter')]
score_type['Average Math Score'][0] = val['Average Math Score'].mean()
score_type['Average Reading Score'][0] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_type['% Passing Math'][0] = val['% Passing Math'].mean()
score_type['% Passing Reading'][0] = val['% Passing Reading'].mean()
score_type['% Overall Passing Rate'][0] = (score_type['% Passing Math'][0] + score_type['% Passing Reading'][0])/2


val = schoolSum_df[(schoolSum_df['School Type'] == 'District')]
score_type['Average Math Score'][1] = val['Average Math Score'].mean()
score_type['Average Reading Score'][1] = val['Average Reading Score'].mean()
total_stu = val['Total Students'].sum()
score_type['% Passing Math'][1] = val['% Passing Math'].mean()
score_type['% Passing Reading'][1] = val['% Passing Reading'].mean()
score_type['% Overall Passing Rate'][1] = (score_type['% Passing Math'][1] + score_type['% Passing Reading'][1])/2

#val
score_type


# In[220]:


topPassing_df = pd.DataFrame(schoolSum_df)
topPassing_df.sort_values(by = '% Overall Passing Rate', inplace = True)
topPassing_df = topPassing_df.head(5)
topPassing_df


# In[221]:


botPassing_df = pd.DataFrame(schoolSum_df)
botPassing_df.sort_values(by = '% Overall Passing Rate', ascending = False, inplace = True)
botPassing_df = botPassing_df.tail(5)
botPassing_df 

