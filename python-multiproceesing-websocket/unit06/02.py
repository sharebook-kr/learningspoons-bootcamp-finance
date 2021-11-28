import threading
import queue
import time
import datetime

def producer(out_q):
    while True:
        data = datetime.datetime.now()
        out_q.put(data)
        time.sleep(1)

def consumer(in_q):
    while True:
        data = in_q.get()
        print(data)
        time.sleep(1)

if __name__ == "__main__":
    q = queue.Queue()
    t1 = threading.Thread(target=producer, args=(q,))
    t2 = threading.Thread(target=consumer, args=(q,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
