import math

def isPrime(n):
    if n < 2:
        return False
    for i in range(2 , int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def fun(n):
    count = 0
    for i in range(2, 10000000):
        if count == n:break
        if isPrime(i) == True:
            string = str(i)
            l , r = 0, len(string) - 1
            flag = True
            while l < r:
                #print(i, ' ', l, ' ', r)
                if string[l] != string[r]:
                    flag = False
                    break
                else:
                    l += 1
                    r -= 1
            if flag:
                print(i, end=' ')
                count += 1
    
fun(eval(input()))

