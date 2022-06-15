str = input()

def func(str):
    if len(str) != 18:
        print('ERROR')
        return  
    if(int(str[16]) % 2 == 0):
        x = '女'
    else:
        x = '男'
    print(str[6:10] + '年' + str[10:12] + '月' + str[12:14] + '日')
    print(x)

func(str)