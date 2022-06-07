str = input()
print('出生：' + str[6:10] + '年' + str[10:12] + '月' + str[12:14] + '日')
if int(str[16]) & 1 == 0:
    print('性别：女')
else:
    print('性别：男')