n = int(input())
list_first =[]
list_total = []
for row in range(n): #构造二维列表，全0填充
    for col in range(n):
        list_first.append(0)
    list_total.append(list_first)
    list_first=[]
list_total[0][int(n/2)]=1 #填入 1
row_forward = 0 #刚填好的数字的行
col_forward = int(n / 2) #刚填好的数字的列
for i in range(2,n*n+1):
    if row_forward -1 < 0:
        row_now = n-1 #第一行 行越界
    else:
        row_now = row_forward -1
    if col_forward +1 > n-1:
        col_now = 0 #最后一列  列越界
    else:
        col_now = col_forward +1
    if list_total[row_now][col_now] != 0: # 如果该位置不是0，则说明该位置已被填好了数字
        row_now = row_forward +1
        col_now = col_forward
    list_total[row_now][col_now]=i
    row_forward = row_now
    col_forward = col_now
for row in list_total:
    for i in range(len(row)):
        if i != len(row) - 1:
            print(row[i], end = ' ')
        else:
            print(row[i], end = '')
    print()