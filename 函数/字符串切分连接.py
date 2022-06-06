def split_and_join(line, sign):  # 在括号里增加参数
    # 你的代码写在这里
    line = line.split()
    res = ''
    for i in range(len(line)):
        res += str(line[i])
        if i != len(line) - 1:
            res += sign
    return res

# 以下代码请勿改动
if __name__ == '__main__':
    line = input()
    sign = input()
    result = split_and_join(line,sign)
    print(result)