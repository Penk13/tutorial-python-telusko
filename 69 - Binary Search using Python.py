# 69 - BINARY SEARCH USING PYTHON

# In binary search, values have to be sorted

list = [4,7,5,88,3,21,90]
n = 21

def bin_search(list,n):
    list.sort()
    print(list)
    L = 0
    U = len(list) - 1

    while L <= U:
        M = (L+U)//2
        if list[M] == n:
            return True
        else:
            if list[M] < n:
                L = M
            else:
                U = M
        return False

if bin_search(list,21):
    print('found')
else:
    print('not found')