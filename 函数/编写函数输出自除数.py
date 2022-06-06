def func(n):
    for i in range(1, n + 1):
        flag = True
        for c in str(i):
            if c == '0':
                flag = False
                break
            if i % int(c) != 0:
                flag = False
                break
        if flag:
            print(i, end=' ')

func(int(input()))