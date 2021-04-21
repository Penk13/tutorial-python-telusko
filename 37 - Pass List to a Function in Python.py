# 37 - PASS LIST TO A FUNCTION IN PYTHON

list = [1,2,3,4,5,6,7,8,9]

def count(list):

    even = 0
    odd = 0
    for i in list:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd

even, odd = count(list)
print('even : {} \n odd : {}'.format(even,odd))

print()

#assignment :
#count how many people that have more than 5 letters from input user

name = []
n = int(input('size of array: '))

for x in range(0,n):
    p = input('enter name:')
    name.append(p)
print(name)


def count2(name):

    a = len(name)
    b = 0
    for j in name:
        c = len(j)
        if c >= 5:
            b += 1
    return b

b = count2(name)
print(b)


