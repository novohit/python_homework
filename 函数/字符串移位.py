def func(str, n):
    if len(str) == 0:
        return ''
    if n >= 0:
        i = len(str) - n % len(str)
    else:
        i = abs(n) % len(str)
    return str[i:] + str[:i]

str = input()
n = eval(input())
print(func(str, n))