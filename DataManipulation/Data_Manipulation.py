import pandas as pd

data = {'Name': ['Jai', 'Princi', 'Gaurav', 
                 'Anuj', 'Ravi', 'Natasha', 'Riya'],
        'Age': [17, 17, 18, 17, 18, 17, 17],
        'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
        'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}

df = pd.DataFrame(data)
print(df)

print("\nDealing with missing values in Python\n")
c=avg=0
for ele in df['Marks']:
    if str(ele).isnumeric():
        c += 1
        avg +=ele
    
avg /= c

df = df.replace(to_replace="NaN",value=avg)
print(df)

print("\nData Replacing in Data Wrangling\n")

df['Gender'] = df['Gender'].map({'M':0,'F':1}).astype(int)

print(df)

print("\nFilter top scoring students\n")

df=df[df['Marks'] >= 75].copy()
df.drop('Age', axis=1, inplace=True)
print(df)

details= pd.DataFrame({
    'ID':[101,102,103,104,105,106,107,108,109,110],
    'Name':['Jagroop', 'Praveen', 'Harjot', 
             'Pooja', 'Rahul', 'Nikita',
             'Saurabh', 'Ayush', 'Dolly', "Mohit"],
    'BRANCH': ['CSE', 'CSE', 'CSE', 'CSE', 'CSE', 
               'CSE', 'CSE', 'CSE', 'CSE', 'CSE'] 
})

fees_status = pd.DataFrame(
    {'ID': [101, 102, 103, 104, 105, 
            106, 107, 108, 109, 110],
     'PENDING': ['5000', '250', 'NIL', 
                 '9000', '15000', 'NIL',
                 '4500', '1800', '250', 'NIL']})

df=pd.merge(details,fees_status,on='ID')
df=df.replace(to_replace="NIL",value=0)
df['PENDING']=df['PENDING'].astype(float)

df = df[df['PENDING']>0].copy()
print(df)

print("\nCreating dataframe to use Grouping methods\n")

car_selling_data = {'Brand': ['Maruti', 'Maruti', 'Maruti', 
                              'Maruti', 'Hyundai', 'Hyundai', 
                              'Toyota', 'Mahindra', 'Mahindra', 
                              'Ford', 'Toyota', 'Ford'],
                    'Year':  [2010, 2011, 2009, 2013, 
                              2010, 2011, 2011, 2010,
                              2013, 2010, 2010, 2011],
                    'Sold': [6, 7, 9, 8, 3, 5, 
                             2, 8, 7, 2, 4, 2]}
df = pd.DataFrame(car_selling_data)
grouping=df.groupby('Year')
# n=int(input("Enter the year:"))
print(grouping.get_group(2010))                        

print("\nCreating a Student Dataset who want to participate in the event\n")

student_data = {'Name': ['Amit', 'Praveen', 'Jagroop', 
                         'Rahul', 'Vishal', 'Suraj',
                         'Rishab', 'Satyapal', 'Amit', 
                         'Rahul', 'Praveen', 'Amit'],
 
                'Roll_no': [23, 54, 29, 36, 59, 38, 
                            12, 45, 34, 36, 54, 23],
 
                'Email': ['xxxx@gmail.com', 'xxxxxx@gmail.com', 
                          'xxxxxx@gmail.com', 'xx@gmail.com', 
                          'xxxx@gmail.com', 'xxxxx@gmail.com', 
                          'xxxxx@gmail.com', 'xxxxx@gmail.com', 
                          'xxxxx@gmail.com', 'xxxxxx@gmail.com',
                          'xxxxxxxxxx@gmail.com', 'xxxxxxxxxx@gmail.com']}

df = pd.DataFrame(student_data)

unique= df [~df.duplicated('Roll_no')]
print(unique)

print("\nCreating New Datasets Using the Concatenation of Two Datasets In Data Wrangling\n")

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd'],
        'Mobile No': [97, 91, 58, 76]} 
     
data2 = {'Name':['Gaurav', 'Anuj', 'Dhiraj', 'Hitesh'], 
        'Age':[22, 32, 12, 52], 
        'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kannuaj'], 
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons'],
        'Salary':[1000, 2000, 3000, 4000]}

df = pd.DataFrame(data1,index=[0, 1, 2, 3])

df1 = pd.DataFrame(data2,index=[2, 3, 6, 7])

res=pd.concat([df,df1])
print(res)
print(res.isnull())

bool_series = pd.isnull(res["Salary"])
print(res[bool_series])

# from pandasgui import show
# df = pd.read_csv("studentdata.csv")
# show(df)

import numpy as np
dict = {'First Score':[100, 90, np.nan, 95], 
        'Second Score': [30, 45, 56, np.nan], 
        'Third Score':[np.nan, 40, 80, 98]} 
df = pd.DataFrame(dict)
print(df.notnull())
print(df.fillna(0))
print(df.fillna(method='pad'))
print(df.fillna(method='bfill'))

data = pd.read_csv("studentdata.csv")
print(data[2:4])

# data["Branch"].fillna("No data", inplace=True)
print(data.info())