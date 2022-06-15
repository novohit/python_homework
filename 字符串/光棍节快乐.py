n = int(input())
n = bin(n)

def func(n):
    return n.count('1')
print(func(n))