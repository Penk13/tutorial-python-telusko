# 60 - METHOD OVERLOADING AND METHOD OVERRIDING

#Method Overloading:

class Student:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def sum(self, a = None, b = None, c = None):    #by default will result none
        s = 0
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s = a+b
        else:
            s = a

        return s

s1 = Student(53,75)
print(s1.sum(67,56,23))

#Method Overriding:

class MyFather:

    def phone(self):
        print("this is my father's phone")

class Me(MyFather):

    def phone(self):
        print("this is my phone")

a = Me()
a.phone()
#it will check the class Me() first,
#if there is no 'phone' function,
#it will take 'phone' function from class MyFather()
