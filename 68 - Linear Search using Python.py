# 68 - LINEAR SEARCH USING PYTHON

inp = int(input('search number : '))
data = [5,6,3,7,9,1]

def search1():
    for i in data:
        if i == inp:
            print('found')
            break
search1()


def search2(n):
    i = 0
    while i < len(data):
        if data[i] == n:
            print('found')
        i += 1
search2(9)


list = [5,2,7,9,8]
pos = -1
def search3(list,a):
    for i in range(len(list)):
        if list[i] == a:
            globals()['pos'] = i
            return True

if search3(list,8):
    print('found at',pos+1)
else:
    print('not found')

