n = int(input())

j = [chr(x) for x in range(ord('A'), ord('Z') + 1)] #将A-Z存入j中
m = n % 26 #取模
str=''
while n != 0:#遍历
    m = n % 26
    if m == 0:
        n = n // 26 - 1
        m = 26
    else:
        n = n // 26
    str = str + j[m - 1]
print(str[::-1])#逆序输出
