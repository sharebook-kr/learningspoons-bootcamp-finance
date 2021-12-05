# Daemon Process
# 메인 프로세스가 종료시 서브 프로세스도 종료됨
import multiprocessing as mp 
import time


def work():
    print("Sub Process start")
    time.sleep(5) 
    print("Sub Process end")


if __name__ == "__main__":
    print("Main Process start")
    proc = mp.Process(name="Sub Process", target=work, daemon=True)
    proc.start()
    print("Main Process end")

