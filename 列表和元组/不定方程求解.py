a, b, c = map(int,input().split())

res = []
x, y = 0, c

# 二分 lgn 只枚举非负数
while x <= c and y >= 0:
    if a * x + b * y == c:
        res.append([x,y])
        x = x + 1
        y = y - 1
    elif a * x + b * y < c:
        x = x + 1
    else:
        y = y - 1
print(res)
print(len(res))