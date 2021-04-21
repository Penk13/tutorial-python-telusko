# 05 - LIST IN PYTHON

# List = wadah untuk menampung beberapa value (mirip array)
# Use []
# Valuenya dapat berupa type data apa saja (integer, string, float, dll)
# Bersifat mutable (dapat mengubah value)

nums = [23,24,25,73,69]
mix = [17, 'penk', 2.5 ]
hallo = [nums,mix]
print(nums[3])	#Output : 73 (memanggil index ke-3 dari list nums)
print(nums[2:])	#Output : 25,73,69 (memanggil index ke-2 sampai terakhir)

# Function in list :
# list.append(value) 		= menambahkan value ke list di index terakhir
# list.insert(index, value) = menambahkan value ke list di index yang ditentukan
# list.remove(value) 		= menghapus value dari list
# list.pop(index) 			= menghapus value yang ditentukan oleh index dari list
# list.pop()				= menghapus value index terakhir dari list
# del list[index]			= menghapus value yang ditentukan oleh index dari list
# nums.extend([value])		= menambahkan value yang ada dalam kurung ke index paling terakhir
# min(list)					= menampilkan nilai terkecil dalam list (integer and float only)
# max(list)					= menampilkan nilai terbesar dalam list (integer and float only)
# sum(list)					= menjumlah semua nilai dalam list (integer and float only)
# nums.sort()				= mengurutkan value dari list dari yang terkecil hingga terbesar

# Example :
nums.append(40)
print('append :', nums)

nums.insert(2,12)
print('insert :', nums)

nums.remove(25)
print('remove :', nums)

nums.pop(2)
print('pop :', nums)

nums.pop()
print('pop()', nums)

del nums[2:]
print('del :', nums)

nums.extend([40,23,7.3])
print('extend :', nums)

print('min :', min(nums))

print('max :', max(nums))

print('sum :', sum(nums))

nums.sort()
print('sort :', nums)