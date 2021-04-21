# 61 - ITERATOR

nums = [3,7,2,9]

for i in nums:
    print(i)

print()

it = iter(nums)
print(it.__next__())
print(it.__next__())
print(next(it))
print(next(it))

print()

class TopTen:

     def __init__(self):
         self.num = 1

     def __iter__(self):
         return self

     def __next__(self):
         if self.num <= 10:
             val = self.num
             self.num += 1
             return val
         else:
             raise StopIteration

values = TopTen()

print(next(values))
for i in values:
    print(i)




