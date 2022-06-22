ls = list(map(int, input().split()))
n = int(input())
if n not in ls:
    print("NOT FOUND")
else:
    # range中的值不会动态改变？
    #for i in range(len(ls)):
    while n in ls:
        ls.remove(n)
    print(ls)