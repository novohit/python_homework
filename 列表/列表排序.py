import random

n = int(input())
random.seed(n)

nums = []
for i in range(10):
    nums.append(random.randint(-100, 100))
nums.sort(key=lambda x: (-1, -x) if x > 0 else (0, x) )
print(nums)