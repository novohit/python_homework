res = []
for i in range(10**3, 10**4):
    if i % 11 == 0:
        num = str(i)
        if (int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]) == 6) and (num[0] != num[1] != num[2] != num[3]):
            res.append(i)
print(len(res))
print(res)