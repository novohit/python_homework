n = eval(input())

res = 0
if n == 1: res = 1
elif n == 2: res = 1 / 2
else:
    fenmu1 = 1
    fenzi2 = 1
    fenmu2 = 2
    fenzi_temp = 0
    fenmu_temp = 0
    res = 1 / 2
    for i in range(2, n):
        fenzi_temp = fenzi2
        fenmu_temp = fenmu2
        fenmu2 = fenmu_temp + fenmu1
        fenzi2 = fenzi_temp + 1

        fenmu1 = fenmu_temp
        res += (-1) ** i * (fenzi2 / fenmu2)

print('{:.6f}'.format(res))   


