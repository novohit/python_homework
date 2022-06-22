import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if (n % i) == 0:
            return False
    return True

def func(n):
    ls = []
    count = 0
    while count != 10:
        if isPrime(n):
            ls.append(n)
            count += 1
        n -= 1
    ls.reverse()
    return ls

ls = func(int(input()))
for i in range(len(ls)):
    if i != len(ls) - 1:
        print(ls[i], end = '+')
    else:
        print(ls[i], end = '=')
print(sum(ls))
