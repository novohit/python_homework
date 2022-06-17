import random

n = int(input())
random.seed(n)
m = random.randint(1, n)

ls = list(range(1, n + 1))
print(ls)

for x in ls:
    if x % m == 0:
        ls.remove(x)
print(ls)