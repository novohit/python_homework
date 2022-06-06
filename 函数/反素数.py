import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def func(n):
    count = 0
    for i in range(2, 10000000):
        if count == n:break
        j = int(str(i)[::-1])
        if i != j and isPrime(i) and isPrime(j):
            print(i, end=' ')
            count += 1
    
func(eval(input()))