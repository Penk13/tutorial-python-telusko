# 16 - IMPORT MATH FUNCTIONS IN PYTHON

import math #import math library
# Isi :
# math.sqrt()	fungsi akar
# math.floor()	fungsi membulatkan angka kebawah
# math.ceil()	fungsi membulatkan angka keatas
# math.pow()	fungsi pangkat
# math.pi 		nilai pi
# and more, go to documentation or type help('math')

print(math.sqrt(25))
print(math.floor(4.7))
print(math.ceil(2.1))
print(math.pow(2,5))
print(math.pi)
print()

import math as m 	#jadi ga perlu ngetik math, tinggal ketik m
print(m.sqrt(25))
print(math.sqrt(25))
print()

from math import sqrt, pow 	#only import sqrt and pow function from math library
print(math.pow(2,3))
print(pow(5,5))

help('math') 