import re


total_money = eval(input())
month = eval(input())
method = input()
month_rate = eval(input())

ls = []
def func(total_money, month, method, month_rate):
    if method == "ACPI":
        ls.append(round((total_money * month_rate * (1 + month_rate) ** month) / ((1 + month_rate) ** month - 1), 2))
        print(ls[0])
    elif method == "AC":
        n = month
        yihuan = 0
        for i in range(n):

            ls.append(round(total_money / month + (total_money - yihuan) * month_rate, 2))
            yihuan = yihuan + (total_money / month)
        print(ls)
    else:
        print("还款方式输入错误")
        return

func(total_money, month, method, month_rate)
