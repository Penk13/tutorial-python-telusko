# 13 - SWAP TWO VARIABLES IN PYTHON

a = 10
b = 5

# Use third variables (wasting memory 1 variables)
temp = a
a = b
b = temp
print(a)
print(b)
print()

# Use this formula (wasting memory 1 bit)
a = a + b #15
b = a - b #10
a = a - b #5
print(a)
print(b)
print()

# Use XOR (no wasting memory)
a = a ^ b
b = a ^ b
a = a ^ b
print(a)
print(b)
print()

# Use ROT_TWO() (only at python) (no wasting memory)
a,b = b,a
print(a)
print(b)

# Note :
# Operator XOR adalah operator yang akan menghasilkan true apabila salah satunya true dan satunya lagi false, akan menghasilkan false jika keduanya true atau keduanya false