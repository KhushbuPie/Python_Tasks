import pandas as pd
import csv
from collections import defaultdict

data = pd.read_csv("data.csv")
df=pd.DataFrame(data)
print(df)

print("\nDealing with missing data\n")
df['CGPA']=df['CGPA'].astype(float)
# print(df['CGPA'])

df1=df['CGPA'].mean()
df=df.dropna()
print(df)
print(df[df.columns[0]].count())

df =df[df['CGPA'] >= 3.7].copy()
print(df[df.columns[0]].count(),"student get greate than or equal to 3.7")
print(df)
df.to_csv("higher_rank.csv")
print()
br=df.Branch.unique()
grouping=df.groupby('Branch')
year=df.Year.unique()
# print(year)


for branch in br:
    print("\n",branch,"\n")
    df1=grouping.get_group(str(branch))
    # print(df1)
    year=df1.Year.unique()

    for y in year:
        group=df1.groupby('Year')
        print("\n",y,"\n")
        df2=group.get_group(y)
        print(df2)
        df2.to_csv("studentdata.txt", mode="a",index=False)
        df2.to_csv("studentdata.pdf", mode="a",index=False)


    
    

