# 暴力
ls = eval(input())
def func(str):
    if str == "O":
        return "乙方胜！"
    else :
        return "甲方胜！"
        
if (ls[0] == ls[1] == ls[2]):
    print(func(ls[0]))
elif (ls[3] == ls[4] == ls[5]):
    print(func(ls[3]))
elif (ls[6] == ls[7] == ls[8]):
    print(func(ls[6]))
elif (ls[0] == ls[3] == ls[6]):
    print(func(ls[0]))
elif (ls[1] == ls[4] == ls[7]):
    print(func(ls[1]))
elif (ls[2] == ls[5] == ls[8]):
    print(func(ls[2]))
elif (ls[0] == ls[4] == ls[8]):
    print(func(ls[0]))
elif (ls[3] == ls[4] == ls[5]):
    print(func(ls[3]))
else:
    print("和局...")
