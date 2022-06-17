import random

n = int(input())
random.seed(n)

nums = []

for i in range(10):
    # randint 是左闭右闭
    nums.append(random.randint(1, 100))
for i in range(10):
    for j in range(i+1,10):
        if nums[j]<nums[i]:
            nums[j], nums[i] = nums[i], nums[j]
print(nums)