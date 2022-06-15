id = input()    # 输入学号
name = input()  # 输入姓名
print(id + name) # 输出学号姓名，中间无空格
print(name * 5)   # 重复输出姓名5遍，中间无空格

s = '人都可以走路，也就是有一个走路方法'  # 这是一个字符串
n = int(input()) # 接收一个整数输入n
print(s[n])       # 输出字符串s中序号为n的字符
for i in range(len(s)):
    if (i & 1) == 0:
        print(s[i], end='')    # 输出字符串s中序号为偶数的字符
print()
print(s[::-1])   # 将字符串逆序输出
print(len(s))     # 输出字符串s的长度
print(len(s[n::])) # 输出字符串s中从序号n到字符串结尾包含的字符个数（包括序号为n的字符）
print(s.count('走路'))  # 输出字符串s中子字符串‘走路’的个数
print(s.index('走'))   # 输出字符串s中字符‘走’第一次出现的位置序号
test = input()          # 输入一个字符串
print(test in s)       # 测试test是否在s中存在，输出测试的结果
#print(s.index('走路方法论'))   # ValueError: substring not found
