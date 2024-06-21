#sorting by value

my_dict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

values=list(my_dict.values())
values.sort()
# print(values)
key=list()
for i in values:
    key.append(my_dict[i])

sorted_dict={i:my_dict[i] for i in key}

print(sorted_dict)

#Write a Python script to add a key to a dictionary.

dictionary={0:10,1:20}
dictionary.update({2:30})
print(dictionary)

##concatenate the following dictionaries to create a new one.

dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}

dic4 ={}
for d in (dic1,dic2,dic3):
    dic4.update(d)
print(dic4)

def is_key(x):
    if x in dic4:
        print(f"{x} present in dictionary")
    else:
        print(f"{x} is not present in dictionary")

# n=int(input("enter the key :"))
# is_key(n)

def maximum():
    dic={1: 10, 2: 20, 3: 30, 4: 80, 5: 50, 6: 60}
    max = dic[1]
    for i in dic:
        if dic[i]>max:
            max=dic[i]
    print(max)  
# maximum()

def frequency():
    d={'V': 10, 'VI': 10, 'VII': 40, 'VIII': 20, 'IX': 70, 'X': 80, 'XI': 40, 'XII': 20}
    val = list(d.values())
    print(val)
    dict1={i:val.count(i) for i in val}
    print(dict1)

frequency()

#calculates the length of the values in a dictionary

def length():
    color_dict = {1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
    val = color_dict.values()
    print(val)
    d1={i:len(i) for i in val}
    print(d1)

length()

#find the highest 3 values of corresponding keys in a dictionary.
def highest3():
    my_dict = {'a': 500, 'b': 587, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
    val=list(my_dict.values())
    max=val[0]
    l=list()
    n=0
    while n<3:
        for i in range(6):
            if val[i]>max:
                max=val[i]
        l.append(max)
        n+=1
        val.remove(val[i])

# highest3()

def iterate():
    d = {'x': 10, 'y': 20, 'z': 30}
    for key,val in d.items():
        print(key ,'->', val)
iterate()

def squeare():
    n = int(input("Enter the number:"))
    dics={i:i*i for i in range(1,n+1)}
    print(dics)

# squeare()

def sumofval():
    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
    l=list(my_dict.values())
    sum = 0
    for i in l:
        sum = sum + i
    print(sum)

sumofval()

def multiple():
    my_dict = {'data1': 100, 'data2': -54, 'data3': 247}
    l=list(my_dict.values())
    mul = 1
    for i in l:
        mul = mul * i
    print(mul)
multiple()

def maplists():
    keys = ['red', 'green', 'blue']
    values = ['#FF0000', '#008000', '#0000FF']

    d2=dict(zip(keys,values))

    print(d2)
maplists()   

def countofletter():
    from collections import defaultdict, Counter
    word= input("Enter the word: ")

    word_dict={}

    for latter in word:
        word_dict[latter]=word_dict.get(latter,0)+1

    print(word_dict)
countofletter()

def patten(n):
    for i in range(1,n+1):
        print('*'*i)
    for j in range(1,n,-1):
        print('*')

# patten(3)

        
