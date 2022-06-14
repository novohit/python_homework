keyboard=[['0',' '],['1', ',','.','?','!'],['2','A','B','C' ], ['3','D','E','F'],['4','G','H','I'] ,
['5','J','K','L'], ['6','M','N','O'],['7','P','Q','R','S' ],
['8','T','U','V'],['9','W','X','Y','Z']]

str = input().split()
res = []
for i in str:
    index = len(i) - 1 # 计算字母的索引
    #
    print(keyboard[int(i[0])][index], end='')