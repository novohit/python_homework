n = int(input())

fenmu = 2
fenzi = 1
if n == 1: print(2.0)
else:
    res = 0
    for i in range(n):
        res += fenmu / fenzi
        temp = fenmu
        fenmu = fenmu + fenzi
        fenzi = temp
    #print('{:.3f}'.format(res))
    #print(res)
    print(round(res, 3))
