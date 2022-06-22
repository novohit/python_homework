ls = ['the lord of the rings','anaconda','legally blonde','gone with the wind']
s = input()        # 输入一个字符
if s == '1':       # 当输入为"1"时，输出元素为0-9的3次方的列表 [0, 1, 8, 27, 64, 125, 216, 343, 512, 729]
    print([x**3 for x in range(10)])
elif s == '2':     # 当输入为"2"时，输出元素为0-9中偶数的3次方的列表 [0, 8, 64, 216, 512]
    print([x**3 for x in range(10) if x & 1 == 0])
elif s == '3':     # 当输入为"3"时，输出元素为元组的列表，元组中元素依次是0-9中的奇数和该数的3次方[(1, 1), (3, 27), (5, 125), (7, 343), (9, 729)]
    print([(x, x**3) for x in range(10) if x & 1 == 1])
elif s == '4':     # 当输入为"4"时，将ls中每个元素单词首字母大写输出['The lord of the rings', 'Anaconda', 'Legally blonde', 'Gone with the wind']
    print([x.capitalize() for x in ls]) #

else:              # 当输入为其他字符时，执行以下语句
    print("结束程序")