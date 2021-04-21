# 22 - BREAK CONTINUE PASS IN PYTHON

# break = keluar dari loop
print('===================== BREAK ========================')

av = 5 #candy available at machine
x = int(input('How many candies do you want ?'))
i = 1
while i <= x :
    if i > av :
        print('out of stock')
        break
    print('candy')
    i += 1
print('thankyou\n')

# continue = melanjutkan jalannya loop
print('===================== CONTINUE ========================')

for lol in range(1,101) :
    if lol % 3 == 0 :
        continue
    print(lol)
print()

# pass = skip
print('===================== PASS ========================')

for tes in range(1,200) :
    if tes % 2 == 0 :
        pass
    else :
        print(tes)
print()

