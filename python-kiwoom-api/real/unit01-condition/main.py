import multiprocessing as mp
from receiver import *


if __name__ == "__main__":
    queue = mp.Queue()

    p = mp.Process(
        target=Receiver, 
        name = "Receiver",
        args = (queue,),
        daemon=True
    )
    p.start()

    while True:
        data = queue.get()
        print(data)