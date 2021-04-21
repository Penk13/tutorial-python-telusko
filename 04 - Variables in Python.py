# 04 - VARIABLES IN PYTHON
# Variable = Box untuk menampung nilai (value)
# Value    = Nilai yang ada dalam box (variable)

# You must assign variable first
# Fetching value of previous operations in interpreter (use _)
# Ex:	x = 2 			#assignment
#		y = 3 			#assignment
#		print(x + 10) 	#akan menghasilkan 12
#		print(_+y) 		#akan menghasilkan 15, karena operasi sebelumnya = 12, lalu ditambah dengan y = 3

# String value to variable
name = 'saya budi'
print(name)
print(name + ' doremi')

# Fetching value of string variable by index number (use [])
# Index start from zero or minus one from behind
# Ex : s (Index = 0 or -9)
#	   a (Index = 1 or -8)
#	   y (Index = 2 or -7)
#	   a (Index = 3 or -6)
#      	 (Index = 4 or -5)
#	   b (Index = 5 oe -4)
#      u (Index = 6 or -3)
#	   d (Index = 7 or -2)
# 	   i (Index = 8 or -1)

print(name[0])    #Output : b karena indexnya 0
print(name[4])    #Output :   karena spasi/space tetap dihitung sebagai 1 index
print(name[-2])   #Output : b karena indexnya 0
print(name[2:])   #Output : ya budi karena memanggil index 2 sampai habis
print(name[2:7])  #Output : ya bu karena memanggil index 2 sampai 6
print(len(name))  #Output : 9 karena len menghitung panjang string

