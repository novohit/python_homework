str = input()
if str[0] == '-':
    str = str[1:]
    str = str[::-1]
    print('-{}'.format(int(str)))
else:
    print(int(str[::-1]))
