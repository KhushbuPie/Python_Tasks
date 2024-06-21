#Write a Pandas program to join the two given dataframes along rows and assign all data.
import pandas as pd
student_data1 = pd.DataFrame({
        'student_id': ['S1', 'S2', 'S3', 'S4', 'S5'],
         'name': ['Danniella Fenton', 'Ryder Storey', 'Bryce Jensen', 'Ed Bernal', 'Kwame Morin'], 
        'marks': [200, 210, 190, 222, 199]})

student_data2 = pd.DataFrame({
        'student_id': ['S4', 'S5', 'S6', 'S7', 'S8'],
        'name': ['Scarlette Fisher', 'Carla Williamson', 'Dante Morse', 'Kaiser William', 'Madeeha Preston'], 
        'marks': [201, 200, 198, 219, 201]})

df = pd.concat([student_data1,student_data2])
print(df)
df1 = pd.concat([student_data1,student_data2],axis=1)
print(df1)

s6 = pd.Series(['S6','Scarlette Fisher',205],index=['student_id', 'name', 'marks'])
combine_data=student_data1._append(s6,ignore_index = True)
print(combine_data)

dicts = [{'student_id': 'S6', 'name': 'Scarlette Fisher', 'marks': 203},
         {'student_id': 'S7', 'name': 'Bryce Jensen', 'marks': 207}]

combine_dict=student_data1._append(dicts, ignore_index=True, sort=False)
print(combine_dict)

merged_data_inner = pd.merge(student_data1,student_data2, on="student_id", how='inner')
merged_data_outer = pd.merge(student_data1,student_data2, on="student_id", how='outer')

print(merged_data_inner)
print(merged_data_outer)

data1 = pd.DataFrame({'key1': ['K0', 'K0', 'K1', 'K2'],
                     'key2': ['K0', 'K1', 'K0', 'K1'],
                     'P': ['P0', 'P1', 'P2', 'P3'],
                     'Q': ['Q0', 'Q1', 'Q2', 'Q3']}) 
data2 = pd.DataFrame({'key1': ['K0', 'K1', 'K1', 'K2'],
                      'key2': ['K0', 'K0', 'K0', 'K0'],
                      'R': ['R0', 'R1', 'R2', 'R3'],
                      'S': ['S0', 'S1', 'S2', 'S3']})
concat_data=pd.concat([data1,data2],axis=0, ignore_index=0)
merge_data_left=pd.merge(data1,data2,how='left', on=['key1','key2'])
merge_data_left1=pd.merge(data2,data1,how='left', on=['key1','key2'])
print(merge_data_left)
print(merge_data_left1)

merge_data_right=pd.merge(data1,data2,how='right', on=['key1','key2'])
merge_data_right1=pd.merge(data2,data1,how='right', on=['key1','key2'])
print(merge_data_right)
print(merge_data_right1)

merge_data =pd.merge(data1,data2,on=["key1",'key2'])
print(merge_data)

s1 = pd.Series([1,2,3],name='col1')
s2 = pd.Series([4,5,6])
s3 = pd.Series([7,8,9],name='col3')

df=pd.concat([s1,s2,s3], axis=1, keys=['column1','column2','column3'])
print(df)


data1 = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
                      'B': ['B0', 'B1', 'B2']},
                     index=['K0', 'K1', 'K2'])

data2 = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
                      'D': ['D0', 'D2', 'D3']},
                     index=['K0', 'K2', 'K3'])

result = data1.join(data2)
print(result)
print(concat_data)

df1 = pd.DataFrame({'A': [None, 0, None], 'B': [3, 4, 5]})
df2 = pd.DataFrame({'A': [1, 1, 3], 'B': [3, None, 3]})
result1=df1.combine_first(df2).astype(int)
print(result1)