import jieba

str = input()
len1 = len(list(str))
len2 = len(jieba.lcut(str))
print(f'中文字符数为{len1}，中文词语数为{len2}。')