n = eval(input())
a1, a2 = 1, 1
for i in range(n):
    print(a1, end=' ')
    a1, a2 = a2, a1 + a2