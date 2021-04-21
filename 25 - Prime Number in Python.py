# 25 - PRIME NUMBER IN PYTHON

num = int(input('enter a number : '))

for i in range(2,num) :
    if num % i == 0 :
        print('not prime')
        break
else :
    print('prime')

# Cara-cara yang lebih efektif dan efisien :

