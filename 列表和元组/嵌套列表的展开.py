ls = eval(input())
res = []
def func(ls):
    for x in ls:
        if type(x) == list:
            func(x)
        else:
            res.append(x)
func(ls)
print(res)
