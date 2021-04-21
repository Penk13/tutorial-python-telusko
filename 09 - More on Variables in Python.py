# 09 - MORE ON VARIABLES IN PYTHON

# Variable adalah sebuah box yang memiliki value dan address


# Address dapat dipanggil menggunakan : id(variable)
num = 10
print(id(num))
print()

# Value yang sama akan menggunakan address yang sama
a = 7
b = a
c = 7
print(id(a))
print(id(b))
print(id(c))
print()

#
a = 5
print(id(a))
print(id(b)) #adress b tidak akan sama dengan a karena a = b belum di assign ulang
print(id(c))
print()

#
b = 1
c = a
print(id(a))
print(id(b))
print(id(c))
print()

#
PI = 3.14
print(type(PI)) #memanggil type data

# Note :
# Setiap angka adalah object. Sebenarnya variable yang akan dihubungkan ke angka, bukan angka ke variable. Object akan dibahas lebih detail nanti
# Setiap object yang tidak terpakai atau tidak ada yang menghubungkannya ke object akan dimasukkan ke dalam garbage collection. Garbage collection akan dibahas lebih detail nanti
# Bisa membuat type data sendiri. Akan dibahas lebih lanjut nanti
