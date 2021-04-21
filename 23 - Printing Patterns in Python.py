# 23 - PRINTING PATTERNS IN PYTHON

for i in range(4) :
    for j in range(3) :
        print('# ',end='')
    print('#')
print()

for n in range(4) :
    for m in range(3) :
        if n > m :
            print('#',end='')
    print('#')
print()

for x in range(4) :
    for y in range(4-x) :
        print('#',end='')
    print()