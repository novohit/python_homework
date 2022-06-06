str = input()
for i in range(len(str)):
    if (i & 1) == 0:
        print(str[i], end='')