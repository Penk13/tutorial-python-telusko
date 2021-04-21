# 54 - INNER CLASS

class Student:  #Outer Class

    def __init__(self, name, num):
        self.name = name
        self.num = num
        self.lap = self.Laptop

    def show(self):
        print(self.name, self.num)
        self.lap('i7', 16)

    class Laptop:   #Inner Class

        def __init__(self, cpu, ram):
            self.cpu = 'i5'
            self.ram = 4

        def show(self):
            print(self.cpu, self.ram)

s1 = Student('penk', 23)
s1.show()

lap1 = Student.Laptop('i5', 8)
lap1.show()

#Syntax :

# create NameOfOuterClass class
#class NameOfOuterClass:

    # Constructor method of outer class
    #def __init__(self):
        #self.NameOfVariable = Value

        # create Inner class object
        #self.NameOfInnerClassObject = self.NameOfInnerClass()

        # create a NameOfInnerClass class

    #class NameOfInnerClass:
        # Constructor method of inner class
        #def __init__(self):
            #self.NameOfVariable = Value


# create object of outer class
#outer = NameOfOuterClass()

