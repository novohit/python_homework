ls = list(map(int, input().split()))

def func(ls):
    odd = []
    even = []
    for x in ls:
        if x & 1 == 1:
            odd.append(x)
        else:
            even.append(x)
    if len(odd) != len(even):
        print("ERROR")
        return
    i = 0
    res = []
    odd.sort()
    even.sort()
    while i != len(odd):
        res.append(even[i])
        res.append(odd[i])
        i += 1
    print(res)

func(ls)