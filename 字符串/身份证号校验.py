ls = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
ID = input()
sum = 0
for i in range(17):
    sum += int(ID[i])*int(ls[i])
if str(ID[17]) == 'X':
    if sum % 11 == 2:
        print('身份证号码校验为合法号码!')
    else:
        print('身份证校验位错误!')
elif (sum % 11 + int(ID[17])) % 11 == 1:
    print('身份证号码校验为合法号码!')
else:
    print('身份证校验位错误!')