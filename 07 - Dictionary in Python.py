# 07 - DICTIONARY IN PYTHON

# Dictionary = mirip list tapi ada unique key untuk setiap value

data = {1: 'penk', 2: 'budi', 4: 'otong'}
print(data[4])
print(data.get(1))
print(data.get(3))
print(data.get(3,'Not Found'))	#jika value di kunci 3 tidak ada, akan menghasilkan Not Found

keys = ['pop', 'rock', 'indie']
values = ['hallo', 'balon', 'api']
data = dict(zip(keys,values))
print(data)
print(data['pop']) #akan mengambil value dari kunci pop

data['bom'] = 'bum'	#akan menambahkan key bom dan value bum ke dalam dictionary data
print(data)

del data['bom'] #menghapus key bom dan valuenya
print(data)

prog = {'JS': 'Atom', 'CS': 'VS', 'python': ['PyCharm','Sublime']} #bisa berisi list
print(prog['python'])
