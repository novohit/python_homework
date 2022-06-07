str = input()
str = str.lower()
code = 'Qs2X'
code = code.lower()
if str == code:
    print('验证码正确')
else:
    print('验证码错误，请重新输入')