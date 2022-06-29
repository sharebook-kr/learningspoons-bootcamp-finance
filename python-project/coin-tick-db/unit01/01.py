import multiprocessing as mp
import pyupbit


if __name__ == "__main__":
    queue = mp.Queue()
    proc = mp.Process(
        target=pyupbit.WebSocketClient,
        args=('ticker', ["KRW-BTC"], queue),
        daemon=True
    )
    proc.start()

    while True:
        data = queue.get()
        print(data)
