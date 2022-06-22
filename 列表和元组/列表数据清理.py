def is_number(value):
    """传入一个字符串为参数，判定其能否转为整数或浮点数类型，返回布尔值."""
    if value.isdigit():
        return True
    try:
        print(value)
        value = eval(value)
        print("ERROR")
        return True
    except:
        return False


def clean_data(data):
    """传入一个元素为字符串的二维列表为参数，若子列表中元素为整数类型的字符串，将其转为整数类型。
    若子列表中元素为浮点数类型字符串，将其转为浮点类型，若存在值为整数的浮点数，将其转为整数类型。
    """
    for ls in data:
        for i in range(len(ls)):
            if is_number(ls[i]):
                ls[i] = eval(ls[i])
    return data


if __name__ == '__main__':
    ls = eval(input())
    print(clean_data(ls))