def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0) 


def days_of_month(date_str):
    map = {'01':'31', '02':'28', '03':'31', '04':'30', '05':'31', '06':'30', '07':'31', '08':'31', '09':'30', '10':'31', '11':'30', '12':'31'}
    year = date_str[:4]
    month = date_str[4:6]
    day = date_str[-2:]
    isLeap = is_leap(int(year))
    if month == '02' and isLeap:
        return 29
    return map[month]


if __name__ == '__main__':
    date_in = input()  # 输入一个年月日
    print(days_of_month(date_in))