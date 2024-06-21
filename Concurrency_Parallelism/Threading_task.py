# Task Title: Implementing a Basic Thread Using a Class
import threading

class ThreadExample(threading.Thread):
    def __init__(self, thread_name, thread_ID):
        threading.Thread.__init__(self)
        self.thread_name = thread_name
        self.thread_ID = thread_ID

    def run(self):
        print(str(self.thread_name) + " " + str(self.thread_ID))

thread1 = ThreadExample("Process1", 1000)
thread2 = ThreadExample("Process2", 2000)

thread1.start()
thread2.start()

print("Exit")


# Task Title: Implementing a Basic Thread Using a Function
from threading import Thread
from time import sleep

def threaded_function(arg):
    for i in range(arg):
        print("running", i)
        sleep(1)

if __name__ == "__main__":
    thread = Thread(target=threaded_function, args=(10,))
    thread.start()
    thread.join()
    print("thread finished...")

# Task Title: Creating a Simple Thread Example with Sleep
import threading
import time

def thread():
    print("\n Enter do_something()")
    time.sleep(2)
    print('\nDone sleeping in Thread\n')

print('\nStart of main Thread')

t1 = threading.Thread(target=thread)
t1.start()
t1.join()

print('\nEnd of main Thread')


# Task Title: Passing Arguments to a Thread Function
import threading
import time

def th1(myarg1):
    print(myarg1)
    time.sleep(2)

t1 = threading.Thread(target=th1, args=(1,))
t1.start()
t1.join()

def th1(myarg1, myarg2, myarg3):
    print(myarg1, myarg2, myarg3)
    time.sleep(2)

t2 = threading.Thread(target=th1, args=(1, 2, 3))
t2.start()
t2.join()

# Task Title: Synchronizing Threads with a Lock
import threading
import time

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
print("Indent:", threading.get_ident()) # Thread identifier for current thread
print("Active thread:", threading.active_count()) 
print("Enumerate:", threading.enumerate()) # Return a list of thread objects currently active
print("Current thread:", threading.current_thread()) 
print("Main thread object:", threading.main_thread())
mydata = threading.local()
mydata.x = 1
print(mydata.x)

thread1.join()
thread2.join()
print("Done")
print("Native Id:", threading.get_native_id()) # Native integral Thread ID

# Task Title: Running Daemon Threads in the Background
import threading
import time

def background_task():
    while True:
        print("Background task running")
        time.sleep(2)

background_thread = threading.Thread(target=background_task)
background_thread.daemon = True
background_thread.start()
print("Is alive:", background_thread.is_alive())
print("Daemon:", background_thread.isDaemon())
time.sleep(5)
print("Main thread finished")

