# 30 - COPYING AN ARRAY IN PYTHON

from numpy import *

print('\n=================== Vectorized Operations ===================')

arr = array([1,2,3,4,5])
arr += 5
print(arr)

arr2 = array([2,7,4,6,3])
arr3 = arr + arr2
print(arr3)

print('\n=================== There is a lot function for array ===================')
print(sin(arr))
print(cos(arr))
print(sum(arr))
print(log(arr))
print(sqrt(arr))
print(min(arr))
print(max(arr))
print(concatenate([arr,arr2]))

print('\n=================== MAIN TOPICS ===================')

print('\n=================== Create an array with same memories ===================')
arr10 = arr #ALIASING
print(arr10)
print(arr)  #have the same values
print(id(arr10))
print(id(arr))  #have the same id, it means that they dont create new memories

print('\n=================== Create an array with different memories ===================')
arr10 = arr.view()  #SHALLOW COPY
arr[2] = 100 #still have the same values
print(arr10)
print(arr)
print(id(arr10))
print(id(arr))
print()

arr10 = arr.copy()  #DEEP COPY
arr[2] = 50 #doesnt have the same values
print(arr10)
print(arr)
print(id(arr10))
print(id(arr))