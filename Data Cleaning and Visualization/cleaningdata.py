# load libraries
import pandas as pd
import re

# loading dataset into pandas dataframe
data = pd.read_csv("the-hello-dataset-fa22.csv")
print(data.head())

# cleaning data
# converting all attributes of column 'Name' in uppercase
data["Name"] = data["Name"].str.upper()
print(data.head())

# converting all attributes of column 'FavoriteColor' in uppercase
data["FavoriteColor"] = data["FavoriteColor"].str.capitalize()
print(data.head(42))

# clearing more than one values using 'space(\s)' in regex
data['FavoriteColor'] = [re.split('\s', i)[0] for i in data['FavoriteColor']]
print(data.head(20))

# clearing month column
data["BirthMonth"] = data['BirthMonth'].replace("1", "Jan")
data["BirthMonth"] = data['BirthMonth'].replace("2", "Feb")
data["BirthMonth"] = data['BirthMonth'].replace("3", "Mar")
data["BirthMonth"] = data['BirthMonth'].replace("4", "April")
data["BirthMonth"] = data['BirthMonth'].replace("5", "May")
data["BirthMonth"] = data['BirthMonth'].replace("6", "June")
data["BirthMonth"] = data['BirthMonth'].replace("7", "July")
data["BirthMonth"] = data['BirthMonth'].replace("8", "Aug")
data["BirthMonth"] = data['BirthMonth'].replace("9", "Sep")
data["BirthMonth"] = data['BirthMonth'].replace("10", "Oct")
data["BirthMonth"] = data['BirthMonth'].replace("11", "Nov")
data["BirthMonth"] = data['BirthMonth'].replace("12", "Dec")
data["BirthMonth"] = data["BirthMonth"].str.capitalize()
data["BirthMonth"] = data['BirthMonth'].replace("Sep", "September")
data["BirthMonth"] = data['BirthMonth'].replace("Oct", "October")
data["BirthMonth"] = data['BirthMonth'].replace("Feb", "February")
data["BirthMonth"] = data['BirthMonth'].replace("Jan", "January")
data["BirthMonth"] = data['BirthMonth'].replace("Aug", "August")
data["BirthMonth"] = data['BirthMonth'].replace("Nov", "November")
data["BirthMonth"] = data['BirthMonth'].replace("Dec", "December")
print(data.head(125))

#cleaning the CGPA column
data['CGPA'] = [re.sub("\.$", "", i) for i in data['CGPA']]
print(data.head())

# cleaning values of weight column using regex
data['Weight'] = [re.sub("kg", "", i) for i in data['Weight']]
data['Weight'] = [re.split("\.", i)[0] for i in data['Weight']]
print(data.head(32))

# defining function to calcute number from given percentage
def number_func(num):
    return (num / 100) * 510

# cleaning HSSC columns
data['HSSC-1'] = [re.split("/", i)[0] for i in data['HSSC-1']]
data['HSSC-2'] = [re.split("/", i)[0] for i in data['HSSC-2']]
data['HSSC-2'] = [re.split(" ", i)[0] for i in data['HSSC-2']]
print(data.head(40))

x = number_func(60)
x = int(x)
data["HSSC-1"] = data['HSSC-1'].replace("60%", x)
print(data.head(43))

data.loc[6, 'HSSC-1'] = '348'
data.loc[9, 'HSSC-1'] = '495'
data.loc[59, 'HSSC-1'] = '378'
data.loc[93, 'HSSC-1'] = '428'
data.loc[103, 'HSSC-1'] = '387'
data.loc[108, 'HSSC-1'] = '373'
data.loc[16, 'HSSC-2'] = '380'
data.loc[28, 'HSSC-2'] = '448'
data.loc[32, 'HSSC-2'] = '529'
data.loc[38, 'HSSC-2'] = '426'
data.loc[57, 'HSSC-2'] = '350'
data.loc[59, 'HSSC-2'] = '377'
data.loc[67, 'HSSC-2'] = '422'
data.loc[68, 'HSSC-2'] = '506'
data.loc[72, 'HSSC-2'] = '524'
data.loc[85, 'HSSC-2'] = '417'
data.loc[90, 'HSSC-2'] = '530'
data.loc[92, 'HSSC-2'] = '524'
data.loc[93, 'HSSC-2'] = '428'
data.loc[95, 'HSSC-2'] = '527'
data.loc[106, 'HSSC-2'] = '418'
data.loc[110, 'HSSC-2'] = '386'
data.loc[112, 'HSSC-2'] = '274'
data.loc[117, 'HSSC-2'] = '445'
data.loc[128, 'HSSC-2'] = '381'
data.loc[131, 'HSSC-2'] = '400'
data.loc[128, 'HSSC-2'] = '381'

#making new file after removing noise from data
data.to_csv('newData.csv')