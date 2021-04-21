# 20 - WHILE LOOP IN PYTHON

i = 1                       # initialization
while i<=5 :                # condition
    print('hello')
    i = i + 1               # increment/decrement

print()
print('========================== 1 ==========================')
print()

i = 1
while i<=5 :
    print('month ',end="")          # end="" means stay at same line
    j = 5
    while j>=1 :
        print('date ',end="")
        j -= 1
    print()
    i += 1
