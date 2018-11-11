'''
https://viblo.asia/p/da-luong-trong-python-multithreading-WAyK8MO6ZxX
Da luong trong Python
'''


#Khong phan luong
import time

def cal_square(numbers):
    print("Calculate square number")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)

def cal_cube(numbers):
    print("Calculate cube number")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n*n)

arr = [2,3,7,9]
t = time.time
cal_square(arr)
cal_cube(arr)
print ("done in ", time.time())


# Mutithreading

from threading import Thread
import threading
import time

def cal_square(numbers):
    print("Calculate square number")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)

def cal_cube(numbers):
    print("Calculate cube number")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n*n)

arr = [2,3,7,9]

try:
    t = time.time()
    t1 = threading.Thread(target= cal_square, args=(arr,))
    t2 = threading.Thread(target= cal_cube, args=(arr,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("done in ", time.time()- t)
except:
    print("error")


# Module Thread
from threading import Thread
import time

class myThread(Thread):
    '''docstring for myThread'''
    def __init__(self, name, counter, delay):
        super(myThread, self).__init__()
        self.name = name
        self.counter = counter
        self.delay = delay
    
    def run(self):
        print("san sang chay" + self.name)
        while self.counter:
            time.sleep(self.delay)
            print("%s: %s" %(self.name, time.ctime(time.time())))
            self.counter -=1
        print ("ket thuc vong lap", self.name)

try:
    thread1 = myThread("thread 1", 10,2)
    thread2 = myThread("thread 2", 10,3)
    thread1.start()
    thread2.start()
except:
    print("Error")

# Module Threading

import threading
import time

def daemon():
    print(threading.currentThread().getName(), 'Starting')
    time.sleep(2)
    print(threading.currentThread().getName(), 'Exiting')

def non_daemon():
    print(threading.currentThread().getName(),'Starting')
    print(threading.currentThread().getName(), 'Exiting')

d = threading.Thread(name='daemon', target=daemon)
d.setDaemon(True)
t = threading.Thread(name = 'non-daemon', target=non_daemon)

d.start()
t.start()

