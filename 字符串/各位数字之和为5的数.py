n = eval(input())
for i in range(n + 1):
    sum = 0
    for c in str(i):
        sum += int(c)
    if sum == 5:
        print(i, end = ' ')