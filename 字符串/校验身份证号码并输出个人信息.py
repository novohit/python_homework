def leap(year):
    return True if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0) else False
 
 
# 校验身证号中的年月日及校验码
def IDcheck(id):
    # 年份超过当前年，或月份小于1或大于12，或日期小于1或大于31时非法
    if int(id[6:10]) > datetime.datetime.now().year or int(id[10:12]) < 1 or int(id[10:12]) > 12 or int(
            id[12:14]) < 1 or int(id[12:14]) > 31:
        return False
    # 当月份为4，6，9，11时，日期超过30即非法
    if int(id[10:12]) in [4, 6, 9, 11] and int(id[12:14]) > 30:
        return False
    # 月份为2时，日期大于29便非法
    if int(id[10:12]) == 2 and int(id[12:14]) > 29:
        return False
    # 月份为2时，如果不是闰年，日期大于28便非法
    if int(id[10:12]) == 2 and leap(year) == False and int(id[12:14]) > 28:
        print(year)
        return False
    # 计算校验和
    ls = [7, 9, 10, 5, 8, 4, 2, 1, 6, 3, 7, 9, 10, 5, 8, 4, 2, 1]
    IDsum = sum([ls[i] * int(id[i]) for i in range(17)])
    if id[17] == 'X':
        return True if IDsum % 11 == 2 else False
    elif (IDsum % 11 + int(id[17])) % 11 == 1:
        return True
    else:
        return False
 
 
import datetime  # 导入datetime模块用于获取当年年份
 
id = input()
year = int(id[6:10])
month = id[10:12]
day = id[12:14]
if len(id) == 18 and IDcheck(id):  # 先判断长度是否是18位，再判断校验和
    gender = '女' if int(id[16]) % 2 == 0 else '男'
    print('身份证号码校验为合法号码!')
    print('出生：{}年{}月{}日'.format(year, month, day))
    # print('年龄：{}'.format(datetime.datetime.now().year - year))
    print('性别：{}'.format(gender))
else:
    print('身份证校验位错误!')