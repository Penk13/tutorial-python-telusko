# 50 - __init__ METHOD

class Computer:

# __init__ is similar to constructors in C++ and Java
# Usages : to initialize (assign value) to the data member of the class when an object of class is created
    def __init__(self, cpu, ram): #every time you assign the object, anything inside init will be called
        print('hello')
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print('computer spec : ', self.ram, self.cpu)

com1 = Computer('i5', 8)
com2 = Computer('i7', 16)

com1.config()
com2.config()

print()

class Person:

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello, my name is ', self.name)

penk = Person('penk')
navin = Person('navin')

penk.say_hello()
navin.say_hello()