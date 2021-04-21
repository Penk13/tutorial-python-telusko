# 49 - CLASS AND OBJECT

class Computer:

    def config(self):
        print('i5, 16GB, 1TB')

# assign object
com1 = Computer()   #com1 is used for parameters to Computer automatically
com2 = Computer()

# call object
Computer.config(com1)
Computer.config(com2)

# call object (more frequently use)
com1.config()   #com1 is used for parameters to config automatically
com2.config()
