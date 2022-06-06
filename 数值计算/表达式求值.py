import math
a = eval(input())
b = eval(input())
c = eval(input())
x = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
print('{:.2f}'.format(x))