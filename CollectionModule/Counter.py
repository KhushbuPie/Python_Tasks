from collections import Counter


# Count the occurence of List, Dictionary and keyword argument

print("List",Counter(['a','b','c','a','a','b','a','a']))

print("Dict", Counter({'a':3,'b':5, 'c':2}))

print("keyword argument:", Counter(a=3 ,b=2, c=5))


# Make a list from the counter element

c = Counter(p=4, q=2, r=0, s=-2)

print("List",list(c.elements()))


# Count the most common element in the string

s='lkseropewdssafsdfafkpwe'
print("most common 4 character:",Counter(s).most_common(4))


# find most common 10 words from given text

text = """The Python Software Foundation (PSF) is a 501(c)(3) non-profit 
corporation that holds the intellectual property rights behind
the Python programming language. We manage the open source licensing 
for Python version 2.1 and later and own and protect the trademarks 
associated with Python. We also run the North American PyCon conference 
annually, support other Python conferences around the world, and 
fund Python related development with our grants program and by funding 
special projects."""

words= text.split()
print("most common:",Counter(words).most_common(10))


#Write a Python program to compare two unordered lists (not sets).

def comapare_lists(x,y):
    return Counter(x)==Counter(y)

n1=[20,10,30,20,30]
n2=[10,20,30,30,20]
print(f"Is {n1} and {n2} list are same: ",comapare_lists(n1,n2))


#Write a Python program to count the number of students in an individual class.

classes = (
    ('V', 1),
    ('VI', 1),
    ('V', 2),
    ('VI', 2),
    ('VI', 3),
    ('VII', 1),
)
Students=Counter(classname for classname,n0_student in classes)

print(Students)


#Write a Python program to count the occurrences of each element in a given list.

li=[[1, 2, 3, 2], [4, 5, 6, 2], [7, 1, 9, 5]]

print(Counter([i for sublist in li for i in sublist]))





# o/p:
# List Counter({'a': 5, 'b': 2, 'c': 1})
# Dict Counter({'b': 5, 'a': 3, 'c': 2})
# keyword argument: Counter({'c': 5, 'a': 3, 'b': 2})
# List ['p', 'p', 'p', 'p', 'q', 'q']
# most common 4 character: [('s', 4), ('e', 3), ('f', 3), ('k', 2)]
# most common: [('the', 6), ('Python', 5), ('and', 5), ('We', 2), ('with', 2), ('The', 1), ('Software', 1), ('Foundation', 1), ('(PSF)', 1), ('is', 1)]
# Is [20, 10, 30, 20, 30] and [10, 20, 30, 30, 20] list are same:  True
# Counter({'VI': 3, 'V': 2, 'VII': 1})
# Counter({2: 3, 1: 2, 5: 2, 3: 1, 4: 1, 6: 1, 7: 1, 9: 1})