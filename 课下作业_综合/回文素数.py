import math
n = int(input())

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

count = 0
for i in range(100000000):
    if count == n:
        break
    if str(i) == str(i)[::-1] and isPrime(i):
        print(i, end=' ')
        count += 1