str1 = input()
rate = float(input())
def func():
    if rate <= 0:
        print('Data error!')
        return
    if str1[-1] == '$':
        print('{:.2f}￥'.format(float(str1[0:-1]) * rate))
        return
    elif str1[-1] == '￥':
        print('{:.2f}$'.format(float(str1[0:-1]) / rate))
        return
    else:
        print('Data error!')
try:
    func()
except:
    print('Data error!')