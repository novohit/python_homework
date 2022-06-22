ls = list(map(int, input().split()))
n = int(input())
if n in ls:
    print("Fail")
else:
    # 特判 最后一位
    if ls[-1] < n:
        print(len(ls))
        ls.append(n)
    for i in range(len(ls)):
        if ls[i] > n:
            ls.insert(i, n)
            print(i)
            break
    
print(ls)