# 35 - KEYWORDED VARIABLE LENGTH ARGUMENTS IN PYTHON (**kwargs)

def person(name, **data):
    print(name)
    for i,j in data.items():
        print(i,j)


person('penk', age=17, city='Bandung', phone_number='08959595721')

print()

def dic(abc, **test):
    print(abc)
    print(test) #"test" is shown in curly brackets {} and also it has a unique keyword
                # which means it is a dictionary
                # And to access each elements in dictionary, we use .items() function

dic('bambank', tes1=12, tes2='xyz', tes3=8.5)
