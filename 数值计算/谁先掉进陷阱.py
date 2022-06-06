skunk = eval(input())
fox = eval(input())
trap = eval(input())

i = 1
while True:
    if i * trap % skunk == 0:
        print('黄鼠狼')
        break
    elif i * trap % fox == 0:
        print('狐狸')
        break
    i += 1