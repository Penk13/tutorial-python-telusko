# 64 - MULTITHREADING

from time import sleep
from threading import *

class Hello(Thread):
    def run(self):
        for i in range(5):
            print('hello')
            sleep(1)

class Hi(Thread):
    def run(self):
        for i in range(5):
            print('hi')
            sleep(1)

a1 = Hello()
a2 = Hi()

a1.start()
sleep(0.2)
a2.start()

a1.join()
a2.join()

print('\nbye')