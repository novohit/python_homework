money = eval(input())
year = eval(input())
year_rate = eval(input())

x = money * (1 + year_rate) ** year - money
print('利息={:.2f}'.format(x))