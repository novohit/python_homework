# 模板仅供参考，可不按些模板写代码
w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

def id15218(id15):
    # 在这里写你的代码
    id17 = id15[:6] + '19' + id15[6:]
    w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    s = 0
    for i in range(len(id17)):
        s += int(id17[i]) * w[i]
    mod = s % 11

    x = '10X98765432'
    return id17 + x[mod]


n = int(input())
with open('id15.txt','r',encoding='utf-8') as file:
    for i in range(n):
        line = file.readline()   # line 的内容是文件中的一行，字符串类型
        # 在这里写你的代码
        id15, name = line.split()
        sep='　'
        print(id15218(id15) + sep + name)