import string

str = input()

def func(str):
    if len(str) > 1:
        print('ERROR')
        return
    if str[0] in string.ascii_lowercase:
        print('小写字母')
    elif str[0] in string.ascii_uppercase:
        print('大写字母')
    elif str[0] in string.digits:
        print('数字')
    else:
        print('其他字符')

func(str)