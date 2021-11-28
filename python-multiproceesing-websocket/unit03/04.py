# fork-join 
import threading 
import time 

class Worker(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name 

    def run(self):
        print("sub thread start", threading.currentThread().getName())
        time.sleep(3)
        print("sub thread end", threading.currentThread().getName())


print("main thread start")

t1 = Worker("1")
t1.start() 
t2 = Worker("2")
t2.start() 

t1.join()
t2.join()
print("main thread end")