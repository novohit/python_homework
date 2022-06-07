a = input()
b = input()

def func(a, b):
    if not a.isalnum() or not b.isalnum():
        print('data error')
        return
    a = int(a)
    b = int(b)
    if a < 1 or a > 9 or b < 0:
        print('data error')
        return
    res = 0
    temp = 0
    for i in range(b):
        temp = temp * 10 + a
        res += temp
    print(res)
func(a, b)
