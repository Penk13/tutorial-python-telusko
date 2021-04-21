# 53 - TYPES OF METHODS

#Instance Methods   #use 'self'
    #Accessor Methods
    #Mutator Methods

#Class Methods  #use 'cls'

#Static Methods

class Student:

    school = 'telusko'

    def __init__(self, n1, n2, n3):
        self.n1 = n1
        self.n2 = n2
        self.n3 = n3

    def avg(self):  #This is Instance Method because it needs 'self'
        return (self.n1 + self.n2 + self.n3)/3

    def get_n1(self):   #This is mutator methods
        return self.n1

    def set_n1(self, value):     #This is accessor methods
        self.n1 = value

    @classmethod
    def getSchool(cls):  #This is class methods
        return cls.school

    @staticmethod
    def info(): #This is static methods
        print('This is student class.. in abc module')

s1 = Student(23,54,74)
s2 = Student(34,75,86)

print(s1.avg())
print(s2.avg())
print(Student.getSchool())
s1.info()
Student.info()



