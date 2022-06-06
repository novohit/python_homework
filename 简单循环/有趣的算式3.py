res = 0
for i in range(9, 1, -1):
    res = res * 10 + (i)
    print(res, 'x 9 +', (i - 2), '=', res * 9 + (i - 2))