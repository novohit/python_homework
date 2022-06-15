ls = list(map(int, input().split()))
ls.sort() # 原地排序 无返回值
for i in range(len(ls)):
    if i != len(ls) - 1:
        print(ls[i], end = ',')
    else:
        print(ls[i])