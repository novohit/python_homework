import random
import math

n = int(input())
random.seed(n)

ls = [(0, 0)]
def func():
    old_x = 0
    old_y = 0
    for i in range(5):
        # x 和 y 要分开写 否则种子不一样
        dx = random.choice([1,-1])
        hx = random.choice([1,2,3,4,5,6,7,8,9,10])
        new_x = old_x + dx * hx
        
        dy = random.choice([1,-1])
        vy = random.choice([1,2,3,4,5,6,7,8,9,10])
        new_y = old_y + dy * vy
        old_x, old_y = new_x, new_y
        ls.append((new_x, new_y))
    print(ls)
def ola_sum():
    sum = 0
    for i in range(1, len(ls)):
        x1, y1 = ls[i - 1]
        x2, y2 = ls[i]
        sum = sum + math.sqrt((x1-x2)**2 +(y1-y2)**2)
    print(round(sum, 2))
func()
ola_sum()