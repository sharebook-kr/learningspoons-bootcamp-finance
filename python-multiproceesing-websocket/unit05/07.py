# arguments 
import multiprocessing as mp

class Worker:
    def __init__(self):
        pass 

    def run(self, value):
        pname = mp.current_process().name
        print(pname, value)

if __name__ == "__main__":
    w = Worker()
    p = mp.Process(name="Sub Process", target=w.run, args=("hello",))
    p.start()
    p.join()
    print("Main Process")