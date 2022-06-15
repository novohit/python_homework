str = input()
str = str[::-1]

for i in range(len(str)):
    if str[i] != '0':
        print(str[i], end = '')