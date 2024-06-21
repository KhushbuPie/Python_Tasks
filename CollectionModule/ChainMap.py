from collections import ChainMap

'''A ChainMap encapsulates many dictionaries into a single unit and returns a list of dictionaries.'''

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

chnmap= ChainMap(d1,d2,d3)

print(chnmap)

print(chnmap['c'])

print("values",chnmap.values)
print("keys",chnmap.keys)

chain = ChainMap(d1,d2)
print(chain) #ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4})

newchain=chain.new_child(d3)
print("newchain:",newchain) #newchain: ChainMap({'e': 5, 'f': 6}, {'a': 1, 'b': 2}, {'c': 3, 'd': 4})
