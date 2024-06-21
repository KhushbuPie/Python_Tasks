from collections import OrderedDict

'''An OrderedDict is also a sub-class of dictionary but unlike dictionary, it remembers the order in which the keys were inserted '''


# Compare Dictionary and OrderedDict

dictionary ={'a':1, 'b':2, 'c':3, 'd':4}

od=OrderedDict({'a':1, 'b':2, 'c':3, 'd':4})
print("Dictionary :", dictionary)
print("OrderderDict :", od)

#pop up one element from dict
dictionary.pop('a')
dictionary['a']=1
print("After remove an element dict",dictionary)

#pop up one element from OrderedDict
od.pop('a')
od['a']=1
print("After remove an element od", od)

print(str(dictionary))
print(str(od))

od = OrderedDict() 
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4
  
print('Before Deleting')
for key, value in od.items(): 
    print(key, value) 
    
# deleting element
od.pop('a')

# Re-inserting the same
od['a'] = 1

print('\nAfter re-inserting')
for key, value in od.items(): 
    print(key, value)


