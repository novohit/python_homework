n = int(input())

# 试除法
def func(n):
    ls = []
    i = 2
    while i <= n // i:
        # i 一定为素数 ，因为枚举到i时，n已经不含有1~i-1的质因子
        if n % i == 0:
            while n % i == 0:
                n //= i
                ls.append(i)
        i += 1
    
    if n > 1:
        ls.append(n)
    return ls

print(func(n))