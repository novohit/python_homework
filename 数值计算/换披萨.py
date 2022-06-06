m = eval(input())
n = eval(input())

m = int(m * 2.54)
n = int(n * 2.54)
big = (m / 2) ** 2
small = (n / 2) ** 2

res = 0
for i in range(1, 100):
    if small * i >= big:
        res = i
        break
print(res)
