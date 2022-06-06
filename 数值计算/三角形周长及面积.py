import math

a = eval(input())
b = eval(input())
c = eval(input())
s = (a + b + c) / 2
area = math.sqrt(s * (s - a) * (s - b) * (s - c))
print('周长={:.2f}'.format(s * 2))
print('面积={:.2f}'.format(area))