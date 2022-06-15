str = input()
print('你出生于' + str[6:10] + '年' + str[10:12] + '月' + str[12:14] + '日')
if int(str[16]) & 1 == 0:
    print('你的性别为女')
else:
    print('你的性别为男')