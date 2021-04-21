# 31 - WORKING WITH MATRIX IN PYTHON

from numpy import *

arr = array([
    [1,2,3,7,8,9],
    [4,5,6,9,8,7]
])

print('\n=================== There are a lot of attribute ===================')
print(arr.ndim)     #will give you the number of dimensions
print(arr.shape)    #will give you (row,columns)
print(arr.size)     #will give you the size of entire array

print('\n=================== Convert array from 2d to 1d ===================')
arr2 = arr.flatten()    #convert array from 2d to 1d
print(arr2)

print('\n=================== Convert array from 1d to 2d ===================')
arr3 = arr2.reshape(3,4) #(row, columns)
print(arr3)     #convert array from 1d to 2d

print('\n=================== Convert array from 1d to 3d ===================')
arr3 = arr.reshape(2,2,3) #artinya (2 array 2d, tiap array ada 2 baris, tiap array ada 3 columns
print(arr3)

print('\n=================== Convert array to matrix format ===================')
m = matrix(arr)
print(m)
print()

m2 = matrix('1,2,3; 4,5,6; 7,8,9')
print(m2)
print(diagonal(m2))  #print diagonal value
print(m2.min())     #give the smallest number
print(m2.max())     #give the biggest number

print('\n=================== Matrix operations ===================')
m3 = matrix('1,2,3; 4,5,6; 7,8,9')
m4 = matrix('2,4,6; 8,1,3; 5,7,9')
m5 = m3 + m4
print(m5)
print()

m6 = m3 * m4
print(m6)