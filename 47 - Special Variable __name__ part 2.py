# 47 - SPECIAL VARIABLE __name__ (PART 2)

from MyModules2 import a1, a2

def fun1():
    a1()
    a2()
    print('from fun1')
    print()

def fun2():
    a2()
    print('from fun2')

def main():
    fun1()
    fun2()

main()