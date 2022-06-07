str = input()
n = eval(input())

def func(n):
    for c in str:
        if c.isalpha():
            if 'a' <= c <= 'z':
                print(chr((ord(c) - ord('a') + n) % 26 + ord('a')), end='')
            elif 'A' <= c <= 'Z':
                print(chr((ord(c) - ord('A') + n) % 26 + ord('A')), end='')
        else:
            print(c, end='')

func(n)
