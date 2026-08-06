nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
big = []
small = []
i = 0
for x in nums:
    if(nums[i] > 5):
        big.append(nums[i])
    else:
        small.append(nums[i])
    i = i + 1

print("lesser than 5 ==> " + str(small))
print("bigger than 5 ==> " + str(big))
