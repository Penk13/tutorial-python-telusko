# ABSTRACT CLASS AND ABSTRACT METHOD IN PYTHON

from abc import ABC, abstractmethod

class Computer(ABC):
    @abstractmethod
    def process(self):
        pass

class Laptop(Computer):
    def process(self):
        print('its running')
        pass

class Phone(Computer):
    pass

com1 = Laptop()
com1.process()  #it will work because there is a method in Laptop class
com2 = Phone()
com2.process()  #it will result an error because there is no method in Phone class or Computer class



# Summary:

# Abstract method = method which only has a declaration and doesnt have definition
# Abstract class = class which only has at least one abstract method

# When you inherit a abstract class as a parent to the child class,
# The child class should define all abstract method present in parent class
# If it is not done then child class also become abstract class automatically

# Python doesnt support abstract class and abstract method,
# So there is a package called ABC(Abstract Base Classes) by which we can make a class or method abstract
