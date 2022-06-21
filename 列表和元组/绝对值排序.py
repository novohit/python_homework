ls = eval(input())
ls = sorted(ls, key = lambda x : (abs(x), x), reverse = True)

for i in range(len(ls)):
    if i != len(ls) - 1:
        print(str(ls[i]) + ",", end='')
    else:
        print(str(ls[i]), end='')