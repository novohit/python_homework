import random

n = int(input())
random.seed(n)

nums = []
for i in range(10):
    nums.append(random.randint(-100, 100))
nums.sort(key=lambda x: (-1, -x) if x > 0 else (0, x))
# 内置sorted返回是新的list 不改变原来对象 列表的成员方法sort()是原地排序（直接改变数组），无返回值。
print(nums)