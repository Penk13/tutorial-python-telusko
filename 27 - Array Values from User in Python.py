# 27 - ARRAY VALUES FROM USER IN PYTHON

from array import *
arr = array('i',[])
n = int(input('enter length of array : '))

for i in range(n) :
    a = int(input('enter values : '))
    arr.append(a)
print(arr)

c = 0
inp = int(input('find number : '))
for c in range(len(arr)) :
    if inp == arr[c] :
        print('index : ',c)
        break
    c += 1

tes = int(input('find number : '))
print(arr.index(tes))


