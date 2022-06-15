n = int(input())
ls = []
for i in range(n + 1):
    ls.append(str(i).count('1'))
print(sum(ls))