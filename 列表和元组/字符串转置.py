str = input()
n = int(input())

def func(str, n):
    ls = []
    col = len(str) // n + 1
    index = 0
    for i in range(n):
        ls_row = []
        for j in range(col):
            if index < len(str):
                ls_row.append(str[index])
            else:
                ls_row.append(None)
            index += 1
        ls.append(ls_row)
    
    res = ''
    for j in range(len(ls[0])):
        for i in range(len(ls)):
            if ls[i][j] == None:
                continue
            res += ls[i][j]
    print(res)

func(str, n)