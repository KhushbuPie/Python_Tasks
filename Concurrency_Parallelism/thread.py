import threading
import time 

# Task 1: Initial Thread (2 seconds)
def thread():
    print(f"\nEnter do_something()")
    time.sleep(2)
    print('\nDone sleeping in Thread\n')

print(f'\nStart of main Thread')

t1 = threading.Thread(target=thread)
t1.start()
t1.join()

print('\nEnd of main Thread')

# Task 2: Single Argument Thread (2 seconds)
def th1(myarg1):
    print(myarg1)
    time.sleep(2)

t1 = threading.Thread(target=th1, args=(1,))
t1.start()
t1.join()

# Task 3: Multiple Arguments Thread (2 seconds)
def th1(myarg1, myarg2, myarg3):
    print(myarg1, myarg2, myarg3)
    time.sleep(2)

t2 = threading.Thread(target=th1, args=(1, 2, 3))
t2.start()
t2.join()

# Task 4: Worker Threads with Lock (3 seconds each due to lock)
def worker(lock, name):
    with lock:
        for i in range(3):
            print(f"{name}:{i}")
            time.sleep(1)

lock = threading.Lock()

thread1 = threading.Thread(target=worker, args=(lock, 'Thread1'), name='Thread1')
thread2 = threading.Thread(target=worker, args=(lock, 'Thread2'), name='Thread2')
thread1.start()
thread2.start()
thread1.join()
thread2.join()

# Task 5: Threading Information (Negligible time)
print("Indent:", threading.get_ident())  # thread identifier for current thread
print("Active thread:", threading.active_count()) 
print("Enumerate:", threading.enumerate())  # return a list of thread objects currently active
print("current thread:", threading.current_thread()) 
print("Main thread object:", threading.main_thread())

mydata = threading.local()
mydata.x = 1
print(mydata.x)
