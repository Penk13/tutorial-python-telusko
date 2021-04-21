# 10 - DATA TYPES IN PYTHON

# ============== 1. None = Variable kosong yang tidak ada valuenya (biasa disebut juga null) ==============

# ============== 2. Numeric = Angka-angka ==============
#	a. Integer = Angka non-decimal
a = 3
print(a)
#	b. Float = Angka decimal
b = 4.5
print(b)
#	c. Complex = Angka plus atau minus bilangan imajiner
c = 7 + 9j
print(c)
#	d. Bool = True (1) or False (0)
d = 6>4
print(d)
print(a>b)
print()

# You can convert value to another type
con = float(b)
print(con)
con2 = complex(a)
print(con2)
con3 = complex(a,b)
print(con3)
print()

# ============== 3. List = Wadah untuk menampung beberapa variable (mirip array di C++) ==============
hello = ['world','budi','siti']
print(hello)
print()


# ============== 4. Tuple = mirip list, tapi bersifat imutable (tidak dapat mengubah value) ==============
nama = ('bambank','rara','siti')
print(nama)
print()


# ============== 5. Set = mirip list, tapi bersifat acak dan tidak support multiple values ==============
num = {52,74,23,90,90}
print(num)
print()


# ============== 6. String = huruf,karakter,kata,kalimat ==============
e = 'soto'
print(e)
print()

# ============== 7. Range = angka berurut ==============
print(list(range(19)))
# range(angka_mulai,angka_terakhir,selisih/beda antar angka)
print(list(range(3,19,2)))
print()

# ============== 8. Dictionary = mirip list, tapi ada unique key untuk setiap value ==============
ok = {'lop': 'hi', 'top':'elon', 'hup':'kol'}
print(ok.keys())	#memanggil key dictionary
print(ok.values())	#memanggil values dictionary
# Fetching values
print(ok['lop'])
print(ok.get('hup'))
