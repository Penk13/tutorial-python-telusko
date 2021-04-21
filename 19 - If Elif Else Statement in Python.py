# 19 - IF ELIF ELSE STATEMENT IN PYTHON

# If Statement
if True :
    print("i'm right")
    print('bye')
    # spasinya harus sama jika ingin membuat beberapa perintah untuk satu kondisi

x = int(8)
check = x % 2
if check == 0 :
    print('Even')
if check == 1 :
    print('odd')

# Agar lebih efisien dari code sebelumnya, gunakan else :
x = int(8)
check = x % 2
if check == 0 :
    print('Even')
else :
    print('odd')

# Nested if
x = int(8)
check = x % 2
if (check == 0) :   #in Python you can use round brackets or not (optional)
    print('Even')
    if x>5 :
        print('great')
    else :
        print('not great')
else :
    print('odd')

# Elif Statement
y = 3
if y == 1 :
    print('one')
elif y == 2 :
    print('two')
elif y == 3 :
    print('three')
else :
    print('four')