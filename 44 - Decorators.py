# 44 - DECORATORS

# Decorators can modify the behavior of function or class

def div(a,b):
    print(a/b)

def smart_div(func):    #func = div function

    #this is the code which i want inside my div :
    def inner(a,b):
        if a < b:
            a,b = b,a
        return func(a,b)

    return inner

div = smart_div(div)

div(2,4)


print()


def hello():
    print('hello')

def add_func(add):

    def add_this():
        print('start')
        add()
        print('ended')

    return add_this

hello = add_func(hello)
hello()