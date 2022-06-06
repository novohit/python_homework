n = eval(input())
a1, a2 = 1, 1
for i in range(n - 2):
    a1, a2 = a2, a1 + a2

print(a2, end=' ')
print('{:.3f}'.format(a1 / a2))
