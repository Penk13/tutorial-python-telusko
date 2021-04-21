# 55 - INHERITANCE

class A(): #This is superclass

    def f1(self):
        print('This is f1')
    def f2(self):
        print('This is f2')

class B(A):    #This is subclass, will include methods from class A

    def f3(self):
        print('This is f3')
    def f4(self):
        print('This is f4')

class C(B):     #This is subclass, will include methods from A and B

    def f5(self):
        print('This is f5')

class D():

    def f6(self):
        print('This is f6')

class E(A,D):   #This is subclass, will include methods from A and D

    def f7(self):
        print('This is f7')

a1 = A()
a1.f2()

b1 = B()
b1.f2()

c = C()
c.f2()

e = E()
e.f2()






