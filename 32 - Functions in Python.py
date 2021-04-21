# 32 - FUNCTIONS IN PYTHON

def greet() :
    print("Hello")
    print("Good Morning!")

greet()

def add(x,y) :
    z = x + y
    print(z)

add(6,9)

def multiply(n,m) :
    a = n * m
    return a

result = multiply(6,9)
print(result)

def add_sub(f,s) :
    p = f + s
    o = f - s
    return p,o

result1, result2 = add_sub(7,5)
print(result1, result2)