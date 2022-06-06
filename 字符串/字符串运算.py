x = int(input())
str = '1\t5\t3\t9\n' 
str = str.strip() # 去除字符串开头结尾的空白字符 可以去掉换行
ls = list(map(int, str.split('\t')))
res = 0
for i in range(len(ls)):
    res += x * ls[i]
print(res)