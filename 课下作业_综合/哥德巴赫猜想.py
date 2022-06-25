import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def func(n):
    for i in range(2, n):
        if isPrime(i) and isPrime(n - i):
            print(n, '=', i, '+', n - i)
            break
    
n = eval(input())
if (n & 1) == 1:
    print('Data error!')
else:
    func(n)