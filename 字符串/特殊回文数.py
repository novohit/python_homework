n=int(input())

def func(n):
    if n < 1 or n > 54:
        print('输入错误，请重新输入！')
        return
    flag = 0
    for i in range(10000,1000000):
        a=str(i)
        b=0
        if a==a[::-1]:#这里的a[::-1]表示把字符串a倒序
           for j in a:
               b+=int(j)
           if b==n:
               print(a)
               flag = 1
    if flag == 0:
        print('无满足条件的数！')
func(n)
