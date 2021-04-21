# 43 - FILTER MAP REDUCE

from functools import reduce

nums = [9,2,5,3,6,4,7,1]
evens = list(filter(lambda n : n%2==0, nums))
print(evens)

doubles = list(map(lambda a : a*2,evens))
print(doubles)

sum = reduce(lambda b,c : b+c, doubles)
print(sum)