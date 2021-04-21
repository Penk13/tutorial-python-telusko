# 40 - RECURSION

# Recursion = A function that calls itself
import sys

print(sys.getrecursionlimit())  # recursion limit is 1000 by default
sys.setrecursionlimit(2000) # change the limit to 2000

i = 0
def rec():

    global i
    i += 1
    print('hello', i)
    rec()

rec()