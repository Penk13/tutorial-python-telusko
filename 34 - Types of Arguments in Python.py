# 34 - TYPES OF ARGUMENTS IN PYTHON

def add(x,y):   #x and y are called formal arguments
    z = x + y
    print(z)

# Formal Arguments = arguments/parameter yg terdapat dalam function definition
# Actual Arguments = arguments/parameter yg terdapat dalam function call
# (Position, Keyword, Default, Variable Length)

def person(name,age=18):    # age is 18 by default
    print(name)
    print(age)

person('penk', 18)  #position
person(age=28, name='penk') #keyword
person('penk')  #default
print()

def sum(a, *b): # *b means you can add multiple value and the form will be tuple
    print(a)    #int
    print(b)    #tuple
    c = a
    for i in b:
        c = c + i
    print(c)

sum(5,6,7,8)    #variable length

