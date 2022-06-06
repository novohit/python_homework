month_lst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
str = input()
str = str.lower().capitalize()
if str in month_lst:
    if str != 'September':
        print(str[0:3], end = '.')
    else:
        print(str[0:4], end = '.')
else:
    print('spelling mistake')