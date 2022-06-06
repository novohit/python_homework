import math



def count(n, x):
    n = str(n)
    res = 0
    for i in range(0, len(n)):
        if i > 0:
            res += int(n[0:i]) * math.pow(10, len(n) - 1 - i)
        if x == int(n[i]):
            res += int(n[i + 1:len(n) - 1])
        elif x < int(n[i]):
            res += math.pow(10, len(n) - 1 - i)
    return res

print(count(122, 2))