# 24 - FOR ELSE IN PYTHON

x = [23,52,65,16,22]

for i in x :
    if i % 5 == 0 :
        print(i)
        break #akan keluar dari loop dan else jg dilewat karena else masih termsk dlm loop
else :
    print('not found')

