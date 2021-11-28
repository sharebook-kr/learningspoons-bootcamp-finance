import time

def make_americano():
    print("americano start", time.strftime('%X'))
    time.sleep(3)
    print("americano end", time.strftime('%X'))

def make_latte():
    print("latte start", time.strftime('%X'))
    time.sleep(5)
    print("latte end", time.strftime('%X'))

def main():
    make_americano()
    make_latte()

main()