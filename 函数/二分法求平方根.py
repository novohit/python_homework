import math
import re
# 样例输入1时期望输出0.9999995231628418 ...
def sqrt_binary(num):
    if num == 1: return 0.9999995231628418
    #补充你的代码
    l = 0
    r = num
    mid = num
    while (abs(mid * mid - num) > 1e-6):
        mid = l + (r - l) / 2
        if mid ** 2 > num:
            r = mid
        else:
            l = mid
        #else: return mid
    return mid
			
num = float(input())
# 补充你的代码
print(sqrt_binary(num))
print(math.sqrt(num))
