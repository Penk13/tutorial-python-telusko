# 70 - BUBBLE SORT IN PYTHON

def sort(nums):

    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp

nums = [6,2,3,8,5,1]
sort(nums)
print(nums)