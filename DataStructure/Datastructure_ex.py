List = [1 ,2 , 3 , 4 , 5 ]

List.append(6)
print(List)
#o/p: [1, 2, 3, 4, 5, 6]

List.extend([7,8])
print(List)
#o/p: [1, 2, 3, 4, 5, 6, 7, 8]

List.insert(0,6)
print(List)
#o/p:[6, 1, 2, 3, 4, 5, 6, 7, 8]

List.remove(6) #it remove first 6
print(List)
#o/p: [1, 2, 3, 4, 5, 6, 7, 8]

# List.remove(9) #it raises a ValueError

List.pop(5) #remove 5th element
print(List)
#o/p:[1, 2, 3, 4, 5, 7, 8]

List.pop() #remove last element
print(List)
#o/p:[1, 2, 3, 4, 5, 7]

x=List.index(3)
print(f"index of 3 is {x}")
#o/p:index of 3 is 2

l=[10,20,30,50,20,40,20,50,60,70]
print(l.index(20,2)) # find 20 after the index 2
#o/p: 4
print(l.index(20,5,7)) #find between index 5 and 7
#o/p: 6

print(l.count(50)) #give occurence of 50
#o/p:2

l.sort() 
print(l) 
#o/p:[10, 20, 20, 20, 30, 40, 50, 50, 60, 70]

l.reverse()
print(l)
# o/p:[70, 60, 50, 50, 40, 30, 20, 20, 20, 10]

l_copy = l.copy()
print("Shallow copy of l :" ,l_copy)
# o/p: Shallow copy of l : [70, 60, 50, 50, 40, 30, 20, 20, 20, 10]

# List as stack 

stack =[3, 4, 5]
stack.append(6)
stack.append(7)
print(stack) #o/p:[3, 4, 5, 6, 7]

stack.pop()
print(stack) #o/p:[3, 4, 5, 6]
    
#List as Queues

from collections import deque
queue = deque(["Apple","Banana","Grapes"])
queue.append("Berry")
print(queue)
#o/p:deque(['Apple', 'Banana', 'Grapes', 'Berry'])

queue.popleft()
print(queue)
#o/p:deque(['Banana', 'Grapes', 'Berry'])

#List Comprehensive

square= [x**2 for x in range(10)]
print(square)
# o/p:[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

pair=[(x,y) for x in [1,2,3] for y in [2, 3, 4] if x!= y]
print(pair)
#o/p:[(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 2), (3, 4)]

matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

transpose=[[row[i] for row in matrix] for i in range(3)]
print(transpose)
#o/p:[[1, 4, 7], [2, 5, 8], [3, 6, 9]]

a=list(zip(*matrix))
print(a)
#o/p:[(1, 4, 7), (2, 5, 8), (3, 6, 9)]

####  Del 

a = [-1, 1, 66.25, 333, 334, 1234.5]
del a[0]
print(a) #o/p:[1, 66.25, 333, 334, 1234.5]

del a[1:3]
print(a) #o/p:[1, 334, 1234.5]

del a[:]
print(a) #o/p:[]

del a #delete an entire variable

#Tupple

tupple=("a",23,"b")

t =12345,54321,'Hello'  #tupple packing

x,y,z = t # tupple or sequence unpacking

# Set

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)
#o/p:{'apple', 'pear', 'banana', 'orange'}

a=set('abcdefg')
print(a)
# o/p:{'c', 'a', 'd', 'f', 'b', 'e', 'g'}

b=set("bcefgh")

print(a-b) #o/p: {'a', 'd'} in a but not in b
print(a|b) #o/p: {'c', 'a', 'b', 'f', 'e', 'g', 'h', 'd'}  a or b
print(a & b) #o/p:{'b', 'g', 'e', 'f', 'c'} a and b
print(a^b) #o/p: {'h', 'a', 'd'}  aor b but not both

#set comprehensions
a={x for x in 'abcde' if x not in 'abc'}
print(a) 
# o/p:{'d', 'e'}

#Dictionary
tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
#o/p:{'jack': 4098, 'sape': 4139, 'guido': 4127}

dict_comprehesion={x:x**2 for x in (2,4,6)}
print(dict_comprehesion)
# o/p:{2: 4, 4: 16, 6: 36}





