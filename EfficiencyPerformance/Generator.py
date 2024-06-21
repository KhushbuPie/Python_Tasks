import time
def generator(ary):
    n = len(ary)
    for i in range(n):
        for j in range(0, n-i-1):
            if ary[j]>ary[j+1]:
                ary[j],ary[j+1]=ary[j+1],ary[j]
        yield ary[j]
            
l1= [64,34,25,12,22,11,90]
start2=time.time()
print(start2)
generator(l1)
end2=time.time()
total2=end2-start2
print("time for generator:",1000*total2)
for k in generator(l1):
    print(k ,end=" ")