ls=["a","b","c","d","f"]
str = input()

def func(str):
    num = str[:-1]
    ch = str[-1].lower()
    if num.isdigit():
        dig = int(num)
        if dig < 1 or dig > 17 or ch not in ls:
            print('输入错误')
            return
    else:
        print("输入错误")
        return
    if ch=="a" or ch=="f":
        print('窗口')
    elif ch=='c' or ch=='d':
        print('过道')
    elif ch=='b':
        print('中间')

func(str)