# daemon thread
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
for i in range(5):
    name = "thread {}".format(i)
    t = Worker(name)
    t.daemon = True
    t.start() 

print("main thread end")