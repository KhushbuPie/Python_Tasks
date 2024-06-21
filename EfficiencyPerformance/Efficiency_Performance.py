import time
def bubble_sort(a):
    start = time.time()
    n = len(a)
    for i in range(n):
        for j in range(0,n-i-1):
            if a[j]>a[j+1]:
                a[j], a[j+1] = a[j+1],a[j]

li=[64, 34, 25, 12, 22, 11, 90]
start=time.time()
print(start)
bubble_sort(li)
end= time.time()
total=end-start
print('time for list:',1000*total)
# print(li)

import numpy as np
arr = np.array([64,34,25,12,22,11,90])

start1=time.time()
print(start1)
bubble_sort(arr)
end1=time.time()
total1=end1-start1
print("time for Numpy array:",1000*total1)


#List and numpy array
#1] space compelexity is O(n+m) or O(2n) bcpz new list is created
import tracemalloc
from memory_profiler import profile

@profile
def list1():
    f=[1,2,3,4,6,5]
    new_f=[]
    for i in f:
        new_f.append(1+i)
    print("new_f:",new_f)
tracemalloc.start()
list1()
print("Memory:",tracemalloc.get_traced_memory())
tracemalloc.stop()

# et=time.time()
# print("time for list:",(et-st))

#2] space complexity O(n)
@profile
def array():
    na = np.array([1,2,3,4,6,5])
    na = na+1
    print(na)

tracemalloc.start()
array()

print("Memory for array:", tracemalloc.get_traced_memory())
tracemalloc.stop()


import os
import psutil

def process_memory():
    process = psutil.Process(os.getpid())
    mem_info = process.memory_info()
    return mem_info.rss

def profile(func):
    def wrapper(*args, **kwargs):
        mem_before = process_memory()
        result = func(*args, **kwargs)
        mem_after = process_memory()
        print("{}:consumed memory: {:,}".format(

            func.__name__,
            mem_before, mem_after, mem_after-mem_before
        ))

        return result
    return wrapper

@profile
def func():
    x = [1]* (10 ** 7)
    y = [2]* (4 * 10 ** 8)
    del x
    return y

func()

import sys
a=200
b=10.2
print("the size of the int variable :",sys.getsizeof(a),"bytes")
print("the size of the decimal/float variable :",sys.getsizeof(b),"bytes")

string= ""
print("the size of the empty string :",sys.getsizeof(string),"bytes")
ch="a"
ch1="ab"
print("the size of the single character :",sys.getsizeof(ch),"bytes")
print("the size of the single character :",sys.getsizeof(ch1),"bytes")

l1=[]
print("the size of the list:",sys.getsizeof(l1),"bytes")
for i in range(10):
    l1.append(i)
    print("the size of the list:",sys.getsizeof(l1),"bytes")

tuple_ = ()
print("The size of the empty tuple is:",sys.getsizeof(tuple_),"bytes.")
tuple_ = (0,)
print("The size of the tuple with 1 element is:",sys.getsizeof(tuple_),"bytes.")
tuple_ = (0,0,)
print("The size of the tuple with 2 elements is:",sys.getsizeof(tuple_),"bytes.")
tuple_ = (0,0,0,)
print("The size of the tuple with 3 element is:",sys.getsizeof(tuple_),"bytes.")

set_ = set()
print("The size of the empty set is:",sys.getsizeof(set_),"bytes.")
for i in range(10):
    set_.add(i)
    print(f"The size of the set with {i+1} element is:",sys.getsizeof(set_),"bytes.")


dict_ = dict()
print("The size of the empty dictionary is:",sys.getsizeof(dict_),"bytes.")
for i in range(10):
    dict_[i]=i
    print(f"The size of the dict with {i+1} element is:",sys.getsizeof(dict_),"bytes.")

def deepgso(ob):
    size = sys.getsizeof(ob)
    if isinstance(ob, (list,tuple,set)):
        for element in ob:
            size+=deepgso(element)
    if isinstance(ob, dict):
        for k,v in ob.items():
            size+=deepgso(k)
            size+=deepgso(v)
    return size

list_=[[1],1,"1"]
print("Space consumed by the list using getsizeof:",sys.getsizeof(list_))
print("Total space consumed by the list:",deepgso(list_))


ar=np.array([])
print("the size of numpy array:",sys.getsizeof(ar))

