# arguments 
import multiprocessing as mp

def work(value):
    pname = mp.current_process().name
    print(pname, value)

if __name__ == "__main__":
    p = mp.Process(name="Sub Process", target=work, args=("hello",))
    p.start()
    p.join()
    print("Main Process")