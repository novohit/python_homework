import math
# 样例输入1时期望输出0.9999995231628418 ...
def sqrt_binary(num, a):
	l, r = 0, num + 0.25
	while True:
		mid = (l + r) / 2
		if abs(mid * mid - num) <= a:
			return mid
		elif mid * mid - num < 0:
			l = mid
		else:
			r = mid
			
num, a = map(float, input().split(','))      # 输入浮点数 n 和计算精度

# 补充你的代码
print('{:.8f}'.format(sqrt_binary(num, a)))
print('{:.8f}'.format(math.sqrt(num)))