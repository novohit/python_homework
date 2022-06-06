import math
n = eval(input())
res = 0
for i in range(1, n + 1):
    res += math.factorial(i)
print(res)