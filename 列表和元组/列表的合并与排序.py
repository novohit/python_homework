ls1 = list(map(int, input().split()))
ls2 = list(map(int, input().split()))
ls1.extend(ls2)
ls1.sort(reverse=True)
print(ls1)