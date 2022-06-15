str = input()
ls = str.split()
n = len(ls)
print(n)
for i in range(n):
    c = ls[i]
    if not c.isalpha():
        print(c[0:-1])
    else:
        print(c)
