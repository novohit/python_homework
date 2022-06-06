def myprint(c, n, str):
    print(c * n)
    ls = str.split('/')
    print(ls[0] + '年' + ls[1] + '月' + ls[2] + '日')
    print(c * n)

c = input()
n = eval(input())
str = input()
myprint(c, n, str)