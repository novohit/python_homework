m = input()
str = input()

def func(str, m):
    for i in range(len(str)):
        if m == str[i]:
            print('index =', i)
            return
    print('Not Found')

func(str, m)