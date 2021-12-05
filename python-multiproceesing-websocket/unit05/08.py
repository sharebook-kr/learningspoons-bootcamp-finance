import multiprocessing as mp 
import time

def work():
    while True:
        print("sub process is running") 
        time.sleep(1)

if __name__ == "__main__":
    p = mp.Process(target=work, name="SubProcess")
    print("Status: ", p.is_alive())

    p.start()
    print("Status: ", p.is_alive())

    time.sleep(5)   # 메인 프로세스 3초 대기
    p.kill()        # 서브 프로세스 종료
    print("Status: ", p.is_alive())

    p.join()        # 메인 프로세스는 서브 프로세스가 종료될 때까지 블록됨
    print("Status: ", p.is_alive())