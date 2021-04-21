# 52 - TYPES OF VARIABLE

# There are 2 types of variable in OOP:
# 1. Instance variable
# 2. Class (Static) Variable

# namespace is an area where you create and store object/variable

class Smartphone():

    #This is global namespace:
    OS = 'Android'  #This is global variable

    #This is instance namespace:
    def __init__(self):
        self.ram = '2GB'  #This is instance variable
        self.storage = '16GB'  #This is instance variable

sp1 = Smartphone()
sp2 = Smartphone()

sp2.storage = '32GB'    #will only change 1 object (sp2)
Smartphone.OS = 'iPhone'    #will change all object

print(sp1.ram, sp1.storage, sp1.OS)
print(sp2.ram, sp1.storage, sp2.OS)






