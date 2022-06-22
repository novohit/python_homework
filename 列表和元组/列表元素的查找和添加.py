str = input()
ls = str.split()
if 'and' not in ls:
    print(str)
else:
    for i in range(len(ls)):
        if ls[i] == 'and':
            ls.insert(i, 'Anna')
            break
    for i in range(len(ls)):
        if i != len(ls) - 1:
            print(ls[i], end=' ')
        else:
            print(ls[i])