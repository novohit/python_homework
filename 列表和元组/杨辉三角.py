# 输出杨辉三角
import math
num=eval(input()) #输入想要计算的杨辉三角形的阶数
n=len(str(int(math.factorial(num)/(math.factorial(int(num/2))*math.factorial(num-int(num/2))))))            #判断最大的数字位数
ls=[]
def yhlist(m):                                                                                              #计算每行的数字
    global ls
    if m==1:
        ls.append(1)
        return ls
    else:
        ls.insert(0,0)
        ls.append(0)
        for i in range(m):
            ls[i]=(ls[i]+ls[i+1])                                                                           #肩上两个数字和      
        return ls
for i in range(1,num+1):
    lt=yhlist(i).copy()                                                                                     #创建新列表，防止旧值被改变
    s=0
    print(" "*(n*(num+1-i)),end="")                                                                         #控制输出格式
    for j in range(i):
        s=s+lt[j]
        print("{:{}}".format(lt[j],n),end=(" "*n))                                                          #最大位数作为间隔与数字输出长度
    print(" "*(n*(num+1-i)),end="")
    print()