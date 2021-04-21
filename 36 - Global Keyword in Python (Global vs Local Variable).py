# 36 - GLOBAL KEYWORD IN PYTHON (GLOBAL VS LOCAL VARIABLE)

print('=========== 1 ===========')
a = 10  #global variable
def something():
    a = 15  #local variable
    print(a)

print(a)
something()
print()



print('=========== 2 ===========')
b = 20
def something2():
    print(b)    #access the global variable inside the function

something2()
print()



print('=========== 3 ===========')
c = 30
print(id(c))    #this is global variable id
def something3():

    c = 25
    x = globals()['c']  #it will take global variable(c)
    print(id(x))    #have the same id as global variable
    print(x)    #30
    globals()['c'] = 100    #change global variable
    print(c)    #it will yield 25 because it takes local variable(c)
    print(id(c))    #this is local variable id

something3()
print(c)    #it will yield 100 because the global variable have change
print()



print('=========== 4 ===========')
# This function modifies the global variable 's'
def f():
    global s    #it means at this function, we use global variable
    print(s,id(s))
    s = "Look for Geeksforgeeks Python Section" #it will change global variable
    print(s,id(s))

# Global Scope
s = "Python is great!"
f()
print(s,id(s))
print()



# This is good example :
print('=========== 5 ===========')
ex = 1

# Uses global because there is no local 'ex'
def f():
    print('Inside f() : ', ex)


# Variable 'ex' is redefined as ex local
def g():
    ex = 2
    print('Inside g() : ', ex)


# Uses global keyword to modify global 'ex'
def h():
    global ex
    ex = 3  #it will change the global variable
    print('Inside h() : ', ex)


# Global scope
print('global : ', ex)
f()
print('global : ', ex)
g()
print('global : ', ex)
h()
print('global : ', ex)
