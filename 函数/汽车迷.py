def Car(year, num, brand = '宝马'): # 括号里补充你的代码
    return f'这是一辆{year}年生产，型号是{num}的{brand}牌汽车。'
# 以下内容不要修改
ls = input().split()  # 根据空格切分输入字符串为列表
print(Car(*ls))       # 调用函数，取列表中的全部数据做参数