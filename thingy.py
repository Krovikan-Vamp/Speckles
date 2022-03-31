import random
from threading import Thread
from time import sleep

x = 0
def new_target():
    global x
    while True:
        print(f'{x}')
        x += random.randrange(1000000, 9999999999)

threads = []
def main():
    x = 0
    for i in range(500):
        t = Thread(target=new_target)
        t.daemon = True
        threads.append(t)

    for i in range(500):
        threads[i].start()

    for i in range(500):
        threads[i].join()

main()