
res = 0
def func(ls):
    global res
    if len(ls) > res:
        res = len(ls)
    for x in ls:
        if type(x) == list:
            func(x)

ls = eval(input())
func(ls)
print(res)