def f(m,n):
    dir = set(n)
    #print(dir)
    for c in m:
        if c not in dir:
            print('NOT FOUND')
            return
    print('FOUND')

m = input()
if m.isalpha():    #完成该条件分支，输入字符串n判断单词m是否可以由n中的某些字符组成
    n = input()
    f(m,n)
else:
    print('ERROR')