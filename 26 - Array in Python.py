# 26 - ARRAY IN PYTHON

# array can change size
# value in array must be the same type

# (Type Code) - (C Type) - (Python Type) - (Min.size in bytes)
# 'b' | signed char      | int                  | 1
# 'B' | unsigned char    | int                  | 1
# 'u' | Py_UNICODE       | Unicode character    | 2
# 'h' | signed short     | int                  | 2
# 'H' | unsigned short   | int                  | 2
# 'i' | signed int       | int                  | 2
# 'I' | unsigned int     | int                  | 2
# 'l' | signed long      | int                  | 4
# 'L' | unsigned long    | int                  | 4
# 'f' | float            | float                | 4
# 'd' | double           | float                | 8

# signed = can't hold negative number
# unsigned = can hold negative number

from array import *     #import all functions from array
vals = array('i',[2,2,3,7,4,9,-10,8])
print(vals)
print(vals.buffer_info())   #give (adress,size)
vals.reverse()  #reverse value (membalikkan value)
print(vals)
print(vals[2])  #print 1 angka sesuai index
for i in vals :
    print(i)
print()

unic = array('u',['a','t','z','r'])
for p in range(len(unic)) :
    print(unic[p])

new = array(vals.typecode, (a for a in vals)) #take one by one value from vals
print(new)
new = array(vals.typecode, (a*a for a in vals)) #same from previous code, but it will give pow
print(new)

o = 0
while o < len(vals) :
    print(vals[o])
    o += 1

