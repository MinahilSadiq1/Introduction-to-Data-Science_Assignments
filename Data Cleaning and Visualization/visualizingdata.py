# load libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import re

#load a style for the graphs
plt.style.use('seaborn-whitegrid')

# loading dataset into pandas dataframe
data = pd.read_csv("newData.csv")
data["Index"] = [f'{i}' for i in range(1,135)]
print(data.head())

#Print the list of all students whose first name starts with letter the 'H'.
new = data['Name'].values
print(new[0:10])
a= []
for itm in new:
    a = (re.findall(r'^[H].*', str(itm)))
    print(a)

print('---------------')
#Print the total number of students who have a three words name (first-middle-surname).
b= []
for itm in new:
    b = (re.findall(r'[A-Z]+\s+[A-Z]+\s+[A-Z]+', str(itm)))
    print(b)

print('----------------')
#Print the percentage of students who have a CGPA of 3.0 or above.
x = data['CGPA'].values
print(x[0:5])
c = 0
total = 134

for i in x:
    if i >= 3.0:
        c = c+1
print('total number of students having 3.0 or above CGPA:', c)
y = c/total
y = y*100
print('Percentage of students having CGPA 3.0 or above:', round(y))

print('---------------------')
# Plot a pie chart to show the ratio of male and female students.
k = data['Gender'].values
f = 0
t = 134

for j in k:
    if j == 'Female':
        f = f+1

print('total females:', f)
m = 0
m = t-f
print('total male:', m)
lab = ['Male', 'Female']
data = [m, f]
plt.pie(data, labels=lab, autopct='%1.1f%%')
plt.title("Pie Chart")
plt.show()

print('---------------------')
# Plot the CGPA of all male students on a histogram with intervals 2.0-2.5, 2.6-3.0, 3.1-3.5, 3.6-4.0.
male_set = data[data['Gender'] == 'Male']
print(male_set.head())

sns.set_style('dark')
sns.histplot(x='CGPA', data = male_set, bins=[2.0,2.6,3.1,3.6,4.0])
plt.show()

print('----------------')
# Plot the HSSC-1 marks of all male vs female students on a scatter plot.
data = data[
    data.Gender.isin(['Female', 'Male'])
].sample(n=134, random_state = 20)
print(data.shape)
sns.set_style('dark')
sns.scatterplot(x='Gender', y='HSSC-1', hue='Gender', style='Gender',  data=data, palette=['Green', 'Orange'])
plt.title('Scatter Plot')
plt.show()

print('----------------')
#Plot the favorite colors of male vs female students on a bar chart.
sns.countplot(x='FavoriteColor',hue='Gender',data=data)
sns.set(rc={'figure.figsize':(10,10)})
plt.title("Bar Chart")
plt.show()

print('-----------------')
#Plot line chart of students and their birth months.
bd = data['BirthMonth']
plt.plot(bd)
plt.ylabel('Students')
plt.xlabel('Birth Month')
plt.title('Line chart')
plt.show()

print('----------------------')
#Create a correlation matrix between HSSC-1 and HSSC-2 marks and then plot on a heatmap.
print(data[['HSSC-1','HSSC-2']].corr())
sns.heatmap(data[['HSSC-1','HSSC-2']].corr(), annot = True, fmt='.2g',cmap= 'coolwarm')
plt.show()

print('----------------------')
# Bonus points: What other things (insights) you can get from the dataset?
#1. we can get the graph of students who have higher weight.
#2. we can also make a graph to differentiate average weight rate between female and male.
#making a countchart of man vs female weight ratio
sns.countplot(x='Weight',hue='Gender',data=data)
sns.set(rc={'figure.figsize':(10,10)})
plt.title("Bar Chart")
plt.show()