# 03 - GETTING STARTED WITH PYTHON

# Start with open IDLE (go to windows and search)

# Arithmetic Operations
# Urutan Operasi Artitmatika (BODMAS) :
# 	1. B = Brackets  ( (), {}, [] )
# 	2. O = Orders    ( x**2, sqrt (x) )
#	3. D = Divide    ( / )
#	   M = Multiply  ( * )
#	4. A = Add       ( + )
#	   S = Substract ( - )

# // = membagi angka, tapi dgn output integer
print('5//2 = ',
      5 // 2)  # menghasilkan angka 2 karena 5/2 adalah 2.5, tetapi karena harus integer maka dibulatkan ke bawah menjadi 2
# ** = power off/exponentiation
print('5**2 = ', 5 ** 2)
# % = modulus (hasil sisa dari pembagian)
print('5%2 = ', 5 % 2)  # menghasilkan angka 1 karena 5/2 adalah paling mendekati 4, 5-4 = 1

print()  # print baris baru
print('ini adalah baris baru', '\n')  # \n = print baris baru

# Data Type
# Integer = Angka non-desimal (Ex : 1, 273, 17, etc)
# Float   = Angka desimal     (Ex : 2.5, 7.3, 1.9, etc)
# String  = Huruf/karakter    (Ex : 'Hello World', 'penk', 'a', '3')

# String Operations
print('===========STRING OPERATIONS===========')
print('penk')
print("penk's laptop")  # jika ingin print tanda petik satu atau dua ('', ""), harus berbeda antara dalam dan luar
print('penk "laptop"')  # jika ingin print tanda petik satu atau dua ('', ""), harus berbeda antara dalam dan luar
print('penk\'s "laptop"')  # string sesudah tanda \ akan diprint seadanya
print('penk' + 'penk')  # string bisa ditambah
print('penk' * 5)  # string bisa dikali
print(r'\docs\penk')  # r = raw string (semua string di belakang huruf r akan di print seadanya)

