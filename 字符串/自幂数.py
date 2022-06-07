n = eval(input())

def func(n):
    # 4 [1000, 10000)
    for i in range(10**(n - 1), 10**n):
        length = len(str(i))
        sum = 0
        temp = i
        while temp != 0:
            one = temp % 10
            sum += one**length
            temp //= 10
        if sum == i:
            print(i)
func(n)