import random

s = int(input())
random.seed(s)

p = int(input())

ls_a = []
ls_b = []

for i in range(5):
    ls_a.append([i + 1, random.randint(0, 100), random.randint(0, 100)])
    ls_b.append([i + 1, random.randint(0, 100)])
    ls_a[i].insert(p , ls_b[i][1])

print(ls_a)