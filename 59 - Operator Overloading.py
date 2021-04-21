# 59 - OPERATOR OVERLOADING

a = 5
b = 6
print(a + b)    #behind the scene : int.__add__(a,b)
print(int.__add__(a,b))

print()

class Student:

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2

    def __add__(self, other):
        a1 = self.n1 + other.n1
        a2 = self.n2 + other.n2
        a3 = Student(a1,a2)
        return a3

    def __gt__(self, other):    #gt = greater then
        r1 = self.n1 + other.n1
        r2 = self.n2 + other.n2
        if r1 > r2:
            return True
        else:
            return False

    def __str__(self):
        return '{} {} '.format(self.n1, self.n2)    #this will replace {} with value inside the format

s1 = Student(41,56)
s2 = Student(53,90)
s3 = s1 + s2    #behind the scene : Student.__add__(s1,s2)
print(s3.n2)

if s1 > s2:
    print('s1 wins')
else:
    print('s2 wins')

print()

a = 10
print(a)    #behind the scene : a.__str__()
print(a.__str__())

print(s1)   #you get value, not address because __str__ methods
