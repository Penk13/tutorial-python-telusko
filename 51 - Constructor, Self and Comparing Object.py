# 51 - CONSTRUCTOR, SELF AND COMPARING OBJECT

class Computer:

    def __init__(self):
        self.name = 'penk'
        self.age = 18

    def update(self):
        self.name = 'budi'

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False

c1 = Computer()
c2 = Computer()

print(id(c1))   #the adress will keep changing
print(id(c2))

c2.name = 'navin'   #change value
print(c1.name)
print(c2.name)

print()

c2.update() #change value
print(c1.name)
print(c2.name)

print()

if c1.compare(c2):
    print('they are same')
    print('c1 age is ', c1.age)
    print('c2 age is ', c2.age)
else:
    print('they are different')
    print('c1 age is ', c1.age)
    print('c2 age is ', c2.age)