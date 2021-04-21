# 38 - FIBONACCI SEQUENCE

def fib(n):

    a = 0
    b = 1
    if n == 1:
        print(a)
    elif n <= 1:
        pass
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c = a+b
            if c <= 100:
                print(c)
                a = b
                b = c
            else:
                pass
fib(100)

#assignment
#bagaimana jika nilai n nya minus
#print hanya nilai yang kurang dari 100