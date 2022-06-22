n, m = map(int, input().split())

ls = []
for i in range(m):
    ls.append(list(map(eval, input().split())))

for i in range(n):
    sum = 0
    for x in ls:
        sum += x[i]
    print(sum / m)