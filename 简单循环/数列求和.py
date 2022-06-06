n = eval(input())
num = 0
sum = 0

for i in range(n):
    num = num * 10 + (i + 1)
    #print(num)
    sum += num

print(sum)