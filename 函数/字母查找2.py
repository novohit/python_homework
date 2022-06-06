def f(m,n):
    for c in m:
        if m.count(c) > n.count(c):
            print('NOT FOUND')
            return
    print('FOUND')

m = input()
# 是否只存在字母
if m.isalpha():
    n = input()
    f(m,n)
else:
    print('ERROR')