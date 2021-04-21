# 29 - WAYS OF CREATING ARRAYS IS NUMPY

from numpy import *

print('=================== array() ===================')
arr = array([[3,4,8,7],[9,6,3,8]])
print(arr)
print(arr.dtype)
arr2 = array([9,2,7,5,3],float)
print(arr2)
print(arr2.dtype)

print('\n=================== linspace() ===================')
# linspace(start,stop,number)
# angka stop dan start termasuk
arr3 = linspace(3,15,5)
print(arr3)
# akan menghasilkan 5 angka dari 3 sampai 15 dengan interval yang sama

print('\n=================== logspace() ===================')
# logspace(start,stop,number
arr4 = logspace(1,6,3)
print(arr4)
# akan menghasilkan 3 angka dari 10**1 sampai 10**6 dengan interval

print('\n=================== arange() ===================')
# arange(start,stop,interval)
# angka start termasuk, angka stop tidak termasuk
arr5 = arange(5,29,3)
print(arr5)
# akan menghasilkan angka dari 5 sampai 29 dengan interval 3

print('\n=================== zeros() ===================')
# give float type by default
arr6 = zeros(5,int)
print(arr6)
# akan menghasilkan 5 angka 0 dengan type int

print('\n=================== ones() ===================')
# give float type by default
arr7 = ones(6)
print(arr7)
# akan menghasilkan 6 angka 1 dengan type float


