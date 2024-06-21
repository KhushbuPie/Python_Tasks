from collections import defaultdict

''' It is used to provide some default values for the key that does not exist and never raises a KeyError. '''
dict1 = defaultdict(int)
l=[1,3,5,2,7,4,2,1,3]

for i in l:
    dict1[i] +=1
print(dict1)

#this key give KeyError because dict not have default value
# d={} 
# for i in l:
#     d[i]+=1
# print(d)

d = defaultdict(list)
for i in range(5):
    d[i].append(i)
print(d)

