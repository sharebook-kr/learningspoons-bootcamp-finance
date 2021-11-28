import multiprocessing as mp
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
    q = mp.Queue() 
    p1 = mp.Process(target=producer, args=(q,))
    p2 = mp.Process(target=consumer, args=(q,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
