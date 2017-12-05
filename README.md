

```python
import pandas as pd
import numpy as np
```


```python
schools_df = pd.read_csv('schools_complete.csv')
students_df = pd.read_csv('students_complete.csv')
students_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Student ID</th>
      <th>name</th>
      <th>gender</th>
      <th>grade</th>
      <th>school</th>
      <th>reading_score</th>
      <th>math_score</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Paul Bradley</td>
      <td>M</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>66</td>
      <td>79</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Victor Smith</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>94</td>
      <td>61</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Kevin Rodriguez</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>90</td>
      <td>60</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Dr. Richard Scott</td>
      <td>M</td>
      <td>12th</td>
      <td>Huang High School</td>
      <td>67</td>
      <td>58</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Bonnie Ray</td>
      <td>F</td>
      <td>9th</td>
      <td>Huang High School</td>
      <td>97</td>
      <td>84</td>
    </tr>
  </tbody>
</table>
</div>




```python
schools_df.head()
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School ID</th>
      <th>name</th>
      <th>type</th>
      <th>size</th>
      <th>budget</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>0</td>
      <td>Huang High School</td>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Figueroa High School</td>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Shelton High School</td>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Hernandez High School</td>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
    </tr>
    <tr>
      <th>4</th>
      <td>4</td>
      <td>Griffin High School</td>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
    </tr>
  </tbody>
</table>
</div>




```python
district_df = pd.DataFrame(columns=['Total Schools','Total Students','Total Budget','Avg Math Score','Avg Reading Score',
                                   '% Passing Math','% Passing Reading','% Overall Passing Rate'
                                  ],index = [0])
district_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Total Schools</th>
      <th>Total Students</th>
      <th>Total Budget</th>
      <th>Avg Math Score</th>
      <th>Avg Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>15</td>
      <td>39170</td>
      <td>$24,649,428.00</td>
      <td>78.99</td>
      <td>81.88</td>
      <td>90.906306</td>
      <td>100.0</td>
      <td>95.453153</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Huang High School</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Figueroa High School</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charter</td>
      <td>1761</td>
      <td>1056600</td>
      <td>600.0</td>
      <td>83.359455</td>
      <td>83.725724</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Shelton High School</td>
    </tr>
    <tr>
      <th>3</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Hernandez High School</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Charter</td>
      <td>1468</td>
      <td>917500</td>
      <td>625.0</td>
      <td>83.351499</td>
      <td>83.816757</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Griffin High School</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Charter</td>
      <td>2283</td>
      <td>1319574</td>
      <td>578.0</td>
      <td>83.274201</td>
      <td>83.989488</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Wilson High School</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Charter</td>
      <td>1858</td>
      <td>1081356</td>
      <td>582.0</td>
      <td>83.061895</td>
      <td>83.975780</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Cabrera High School</td>
    </tr>
    <tr>
      <th>7</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>87</td>
      <td>100</td>
      <td>93</td>
      <td>Bailey High School</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Charter</td>
      <td>427</td>
      <td>248087</td>
      <td>581.0</td>
      <td>83.803279</td>
      <td>83.814988</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Holden High School</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Charter</td>
      <td>962</td>
      <td>585858</td>
      <td>609.0</td>
      <td>83.839917</td>
      <td>84.044699</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Pena High School</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Charter</td>
      <td>1800</td>
      <td>1049400</td>
      <td>583.0</td>
      <td>83.682222</td>
      <td>83.955000</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Wright High School</td>
    </tr>
    <tr>
      <th>11</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Rodriguez High School</td>
    </tr>
    <tr>
      <th>12</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Johnson High School</td>
    </tr>
    <tr>
      <th>13</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>87</td>
      <td>100</td>
      <td>93</td>
      <td>Ford High School</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Charter</td>
      <td>1635</td>
      <td>1043130</td>
      <td>638.0</td>
      <td>83.418349</td>
      <td>83.848930</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
      <td>Thomas High School</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>77</td>
      <td>75</td>
      <td>76</td>
      <td>77</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>76</td>
      <td>76</td>
      <td>76</td>
      <td>77</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>83</td>
      <td>82</td>
      <td>83</td>
      <td>83</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
      <td>77</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>82</td>
      <td>84</td>
      <td>83</td>
      <td>83</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>83</td>
      <td>83</td>
      <td>83</td>
      <td>83</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>83</td>
      <td>83</td>
      <td>82</td>
      <td>83</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>77</td>
      <td>76</td>
      <td>77</td>
      <td>76</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>83</td>
      <td>83</td>
      <td>85</td>
      <td>82</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83</td>
      <td>83</td>
      <td>84</td>
      <td>84</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>83</td>
      <td>84</td>
      <td>83</td>
      <td>83</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>76</td>
      <td>76</td>
      <td>76</td>
      <td>77</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>77</td>
      <td>76</td>
      <td>77</td>
      <td>76</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>77</td>
      <td>77</td>
      <td>76</td>
      <td>76</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>83</td>
      <td>83</td>
      <td>83</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>9th</th>
      <th>10th</th>
      <th>11th</th>
      <th>12th</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Huang High School</td>
      <td>81</td>
      <td>81</td>
      <td>81</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Figueroa High School</td>
      <td>81</td>
      <td>81</td>
      <td>80</td>
      <td>81</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Shelton High School</td>
      <td>84</td>
      <td>83</td>
      <td>84</td>
      <td>82</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Hernandez High School</td>
      <td>80</td>
      <td>80</td>
      <td>81</td>
      <td>80</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Griffin High School</td>
      <td>83</td>
      <td>83</td>
      <td>84</td>
      <td>84</td>
    </tr>
    <tr>
      <th>5</th>
      <td>Wilson High School</td>
      <td>83</td>
      <td>84</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>6</th>
      <td>Cabrera High School</td>
      <td>83</td>
      <td>84</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>7</th>
      <td>Bailey High School</td>
      <td>81</td>
      <td>80</td>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <th>8</th>
      <td>Holden High School</td>
      <td>83</td>
      <td>83</td>
      <td>83</td>
      <td>84</td>
    </tr>
    <tr>
      <th>9</th>
      <td>Pena High School</td>
      <td>83</td>
      <td>83</td>
      <td>84</td>
      <td>84</td>
    </tr>
    <tr>
      <th>10</th>
      <td>Wright High School</td>
      <td>83</td>
      <td>83</td>
      <td>84</td>
      <td>84</td>
    </tr>
    <tr>
      <th>11</th>
      <td>Rodriguez High School</td>
      <td>80</td>
      <td>80</td>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <th>12</th>
      <td>Johnson High School</td>
      <td>81</td>
      <td>80</td>
      <td>80</td>
      <td>81</td>
    </tr>
    <tr>
      <th>13</th>
      <td>Ford High School</td>
      <td>80</td>
      <td>81</td>
      <td>80</td>
      <td>80</td>
    </tr>
    <tr>
      <th>14</th>
      <td>Thomas High School</td>
      <td>83</td>
      <td>84</td>
      <td>83</td>
      <td>83</td>
    </tr>
  </tbody>
</table>
</div>




```python
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

```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>577.923 - 597.25</td>
      <td>83.4554</td>
      <td>83.9338</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>597.25 - 616.5</td>
      <td>83.5997</td>
      <td>83.8852</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>2</th>
      <td>616.5 - 635.75</td>
      <td>80.2</td>
      <td>82.4254</td>
      <td>93.5</td>
      <td>100</td>
      <td>96.75</td>
    </tr>
    <tr>
      <th>3</th>
      <td>635.75-655.0</td>
      <td>77.8667</td>
      <td>81.3688</td>
      <td>88.1429</td>
      <td>100</td>
      <td>94.0714</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Size</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Small (&lt;1943)</td>
      <td>83.5024</td>
      <td>83.8831</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Medium (1943-3459)</td>
      <td>78.4295</td>
      <td>81.7691</td>
      <td>89.75</td>
      <td>100</td>
      <td>94.875</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Large (&gt;3459)</td>
      <td>77.0633</td>
      <td>80.9199</td>
      <td>86.25</td>
      <td>100</td>
      <td>93.125</td>
    </tr>
  </tbody>
</table>
</div>




```python
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
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Charter</td>
      <td>83.4739</td>
      <td>83.8964</td>
      <td>100</td>
      <td>100</td>
      <td>100</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>76.9567</td>
      <td>80.9666</td>
      <td>86.2857</td>
      <td>100</td>
      <td>93.1429</td>
    </tr>
  </tbody>
</table>
</div>




```python
topPassing_df = pd.DataFrame(schoolSum_df)
topPassing_df.sort_values(by = '% Overall Passing Rate', inplace = True)
topPassing_df = topPassing_df.head(5)
topPassing_df
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>District</td>
      <td>2917</td>
      <td>1910635</td>
      <td>655.0</td>
      <td>76.629414</td>
      <td>81.182722</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Huang High School</td>
    </tr>
    <tr>
      <th>1</th>
      <td>District</td>
      <td>2949</td>
      <td>1884411</td>
      <td>639.0</td>
      <td>76.711767</td>
      <td>81.158020</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Figueroa High School</td>
    </tr>
    <tr>
      <th>3</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Hernandez High School</td>
    </tr>
    <tr>
      <th>7</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>87</td>
      <td>100</td>
      <td>93</td>
      <td>Bailey High School</td>
    </tr>
    <tr>
      <th>11</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Rodriguez High School</td>
    </tr>
  </tbody>
</table>
</div>




```python
botPassing_df = pd.DataFrame(schoolSum_df)
botPassing_df.sort_values(by = '% Overall Passing Rate', ascending = False, inplace = True)
botPassing_df = botPassing_df.tail(5)
botPassing_df 
```




<div>
<style>
    .dataframe thead tr:only-child th {
        text-align: right;
    }

    .dataframe thead th {
        text-align: left;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>School Type</th>
      <th>Total Students</th>
      <th>Total School Budget</th>
      <th>Per Student Budget</th>
      <th>Average Math Score</th>
      <th>Average Reading Score</th>
      <th>% Passing Math</th>
      <th>% Passing Reading</th>
      <th>% Overall Passing Rate</th>
      <th>name</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>3</th>
      <td>District</td>
      <td>4635</td>
      <td>3022020</td>
      <td>652.0</td>
      <td>77.289752</td>
      <td>80.934412</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Hernandez High School</td>
    </tr>
    <tr>
      <th>7</th>
      <td>District</td>
      <td>4976</td>
      <td>3124928</td>
      <td>628.0</td>
      <td>77.048432</td>
      <td>81.033963</td>
      <td>87</td>
      <td>100</td>
      <td>93</td>
      <td>Bailey High School</td>
    </tr>
    <tr>
      <th>11</th>
      <td>District</td>
      <td>3999</td>
      <td>2547363</td>
      <td>637.0</td>
      <td>76.842711</td>
      <td>80.744686</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Rodriguez High School</td>
    </tr>
    <tr>
      <th>12</th>
      <td>District</td>
      <td>4761</td>
      <td>3094650</td>
      <td>650.0</td>
      <td>77.072464</td>
      <td>80.966394</td>
      <td>86</td>
      <td>100</td>
      <td>93</td>
      <td>Johnson High School</td>
    </tr>
    <tr>
      <th>13</th>
      <td>District</td>
      <td>2739</td>
      <td>1763916</td>
      <td>644.0</td>
      <td>77.102592</td>
      <td>80.746258</td>
      <td>87</td>
      <td>100</td>
      <td>93</td>
      <td>Ford High School</td>
    </tr>
  </tbody>
</table>
</div>


