s = input()       # 输入一个英文字符串
print(s.upper())  # 将字符串中所有英文字符转为大写输出
print(s.lower())  # 将字符串中所有英文字符转为小写输出
t = s.split()     # 将输入的字符串根据空格切分为列表，命名为t,每个单词为一个元素
print(t)         # 输出切分的列表
print(' '.join(t)) # 将列表t中的元素用空格连接后输出
print('-'.join(t)) # 将列表t中的元素用连字符“-”连接后输出
print('/'.join(t)) # 将列表t中的元素用'/'连接后输出
print(s.find('the')) # 搜索字符串s中是否存在字符串'the'，如存在返回其位置序号
r = s.replace('the', 'a') # 将字符串s中所有的'the'替换为'a'，替换后的字符串重新命名为r
print(r)             # 输出替换后的字符串r
r = s.replace('the', 'a', 1)# 将字符串s中的第一个'the'替换为'a'，替换后的字符串重新命名为r
print(r)            # 输出替换后的字符串r