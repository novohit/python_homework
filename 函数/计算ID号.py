import math

'''
# 超时
def isPrime(n):          # 定义判断素数的函数
    # 补充你的代码在这里
    if n == 1: return False
    if n == 2: return True
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
'''


# 试除法
def isPrime(n):
    if n < 2:
        return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def func(n):
    # 优化一层循环
    for i in range(1, n):
        if isPrime(i)  and n % i == 0 and i > (n // i) and isPrime(n // i):
            return str(i) + str(n // i)

'''
# 1-n x出现的次数 n*lgn会超时
def count(n, x):
    res = 0
    for i in range(1, n + 1):
        j = i
        while j != 0:
            if j % 10 == x: res += 1
            j //= 10
    return res
'''
# lgn
def count(n, x):
    res = 0
    for i in range(len(str(n))):
        d = int(str(n)[-i - 1])
        res += n // 10 ** (i + 1) * 10 ** i
        if x == d:
            res += n % 10 ** i + 1
        if x < d:
            res += 10 ** i
    return res
    
id = func(eval(input()))
n = eval(input())

print('WHUT' + id)
print(count(int(id), n))