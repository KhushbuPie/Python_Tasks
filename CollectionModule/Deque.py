from collections import deque

dq = deque([1,2,3])
dq.append(4)
print("append:",dq) # append: deque([1, 2, 3, 4])
dq.appendleft(5)
print("appendleft:",dq) #appendleft: deque([5, 1, 2, 3, 4]) 

dq.pop()
print("pop:",dq) # pop: deque([5, 1, 2, 3])

dq.popleft()
print("popleft:",dq) # popleft: deque([1, 2, 3])


# iterate over the deque's elements.
from collections import deque
dq = deque('aeiou')
for i in dq:
    print(i)