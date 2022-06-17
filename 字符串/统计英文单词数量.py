# 分析
# 英文句子中的单词间是用空格分隔的，可以根据空格切分字符串为列表，输出列表的长度即是单词的数量
# 考虑到部分标点符号后可能缺少空格和类似 is't 等形式的缩写，把所有标点符号替换为空格再进行切分
# 所有标点可以用string.punctuation，也可以用'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'表示

s = input()                                     # 输入一个字符串
for c in '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':  # 遍历标点符号，将字符串中的符号替换为空格
	s = s.replace(c, ' ')                       # 替换后的字符串仍命名为s
print(len(s.split()))                           # 根据空格将字符串切分为列表，输出列表的长度

import string

s = input()
for i in string.punctuation:
	s = s.replace(i, ' ')
print(len(s.split()))