import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def func(n):
    res = 0
    count = 0
    for i in range(n, 0, -1):
        if count == 10:
            break
        if isPrime(i):
            res += i
            count += 1
    return res

n = eval(input())
print(func(n))