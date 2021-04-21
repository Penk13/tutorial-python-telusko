# 56 - CONSTRUCTOR IN INHERITANCE

#If you create an object of subclass, it will first try find init of subclass
#If it is not found, it will call init of superclass

class A:

    def __init__(self):
        print('this is init in A')

    def f1(self):
        print('this is f1')

    def f2(self):
        print('this is f2')

class B(A):

    def __init__(self):
        super().__init__()  #super() can call anything in superclass
        print('this is init in B')

    def f3(self):
        print('this is f3')

    def f4(self):
        print('this is f4')

a1 = B()
print()


#Method Resolution Order (MRO)

class C:

    def __init__(self):
        print('this is init in C')

    def func(self):
        print('this is func-C')

class D:

    def __init__(self):
        print('this is init in D')

    def func(self):
        print('this is func-D')

class E(C, D):  #C is on the left, D is on the right

    def __init__(self):
        super().__init__()  #It will call init C, not D
        print('this is init in E')

    def f5(self):
        print('this is f5')

x = E() #it will call init C and E, not D, because MRO will execute from left to right)
x.func()    #it will call func methods from class C, not D


