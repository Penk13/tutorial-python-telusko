# 41 - FACTORIAL USING RECURSION

def rec(n):
    if n == 0:
        return 1
    else:
        return n * rec(n-1)


print(rec(5))