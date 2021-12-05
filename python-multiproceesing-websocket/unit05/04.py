import multiprocessing as mp 
import time


def work():
    print("Sub Process start")
    time.sleep(5) 
    print("Sub Process end")


if __name__ == "__main__":
    print("Main Process start")
    proc = mp.Process(name="Sub Process", target=work)
    proc.start()
    proc.join()
    print("Main Process end")

