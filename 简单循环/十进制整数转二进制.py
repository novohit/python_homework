import math
n = eval(input())

'''
# 使用整形会溢出
res = 0
i = 0
while n != 0:
    res = res + (math.pow(10, i) * (n % 2))
    n //= 2
    i += 1
'''

res = ''
if n == 0:
    print('0')
else:
    while n != 0:
        res += str(n % 2)
        n //= 2
print(res[::-1])