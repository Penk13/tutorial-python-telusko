# 63 - EXCEPTION HANDLING

# There are 3 different types of errors :
# 1. Compile Time
# 2. Logic
# 3. Run Time

# Compile Time Error:
# You will get error at compile time
# Ex : missing (:), wrong spelling

# Logical Error:
# Ex : wrong output
def add(a,b):
    print('number 1 + number 2 = ', a*b)

add(int(input('number 1 : ')), int(input('number 2 : ')))

# Run time Error:
# Ex : wrong input
def div(c,d):
    print('number 1 / number 2 = ', c/d)

div(int(input('number 1 : ')), int(input('number 2 : ')))
# if user input for number 2 is 0, it will result run time error

print()

# Handle error:
a = int(input('input number : '))
b = int(input('input number : '))

# if try block result an error, it will jump to the except block and skip the rest:
try:
    print('file open')
    print(a/b)
    i = int(input('input number : '))   #if users input is not integer type, it will execute except ValueError block
    print(i)

except ZeroDivisionError as e:  #ZeroDivisionError is specific error
    print('You cant divide a number by zero', e)    # e will print what is the error
except ValueError as a: # ValueError is specific error
    print('invalid input')
except Exception as b:  # Exception is for all error
    print('Something wrong...')

finally:
    print('file closed')

# finally block will always executed no matters whether we get an error or not

print('bye')