import multiprocessing as mp 
import time 

def work():
    proc = mp.current_process()
    print(proc.name, proc.pid)
    time.sleep(5)
    print("sub process end")


if __name__ == "__main__":
    # main process
    proc = mp.current_process()
    print(proc.name, proc.pid)

    # process spawning
    p = mp.Process(target=work, name="sub proc")
    p.start()
    print("main process end")