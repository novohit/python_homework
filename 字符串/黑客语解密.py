table = ''.maketrans('0134567', 'oieasgt')  # 创建映射表
keys = input()
print(keys.translate(table))  # 替换字符