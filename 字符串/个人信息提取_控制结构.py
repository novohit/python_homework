s = input()
name = s[14:16]
grade = s[17:23]

for i in range(27, len(s)):
    if s[i:i + 4].isdigit():
        born = s[i:i + 4]
print('姓名：' + name + '\n班级：' + grade + '\n出生：' + born + '年')
