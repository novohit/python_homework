import math
import itertools
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# 暴力枚举所有长度为3的素数组合
def group(ls):
    temp = []
    for i in itertools.combinations(ls, 3):
        temp.append(i)
    return temp

def func(group):
    res = []
    # 将组合中的和放入列表
    for i in group:
        sum = i[0]**2 + i[1]**2 + i[2]**2
        res.append(sum)
    
    # 寻找出现6次的和值
    i = 0
    while True:
        if res.count(i) == 6:
            return i
        i += 1
# 存入不超过100的素数
ls = []
for i in range(2, 101):
    if isPrime(i):
        ls.append(i)

group = group(ls)
print(func(group))