n = eval(input())
str = input()
def func(str, n):
    col = 0
    #  col[0, n]
    if len(str) % n == 0:
        col = len(str) // n - 1
    else:
        col = len(str) // n

    # 观察一列 低头思故乡 发现行是顺序
    for i in range(n):
        # 观察一行 低举疑床 对应原句为逆序 col-0
        for j in range(col, -1, -1):
            # 如果最后一列不足N个，补充空格
            if len(str) <= j * n + i:
                print(" ", end='')
            else:
                print(str[j * n + i], end='')
        print()

func(str, n)