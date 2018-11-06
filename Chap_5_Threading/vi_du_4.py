import threading
import time

exitFlag = 0

class MyThread (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter

    def run(self):
        print("Starting" + self.name)
        print_time(self, threadName=self.name, delay=self.counter, counter=5)
        print("Exiting " + self.name)

def print_time(self,threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s: %s" %(threadName, time.ctime(time.time())))
        counter -= 1

# Create new threads
thread1 = MyThread(1,"Thread-1", 1)
thread2 = MyThread(2, "Thread-2", 2)

# Start new threads
thread1.start()
thread2.start()
thread1.join()
thread2.join()
print("Exiting main thread")

