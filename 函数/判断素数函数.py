import math

# 试除法
def isPrime(n):
    if n < 2:
        return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
    
num = int(input())       # 接收用户输入并转成整数
# 补充你的代码在这里
for i in range(1, num + 1):
    if isPrime(i):
        print(i, end=' ') 