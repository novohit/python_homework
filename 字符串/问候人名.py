import string

str = input()

def func(str):
    name = ''
    if str[0] in string.ascii_letters:
        name += str.title()
    else:
        name += str
    print('Hello,' + name + '!')

func(str)