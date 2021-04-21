# ZIP FUNCTION IN PYTHON

names = ['budi','andi','toni']
num = [90,75,80]

zipped = list(zip(names,num))

print(zipped)
for (a,b) in zipped:
    print(a,b)
