import copy
ls1 = list(input())
ls2 = list(input())
temp = copy.deepcopy(ls1)
temp.extend(ls2)
print(temp)
print(ls1 * 3)
print(ls2[2], ls2[-1])
print(ls1[1:4])
print(f"{len(ls1)},{len(ls2)}")
print(min(ls1), max(ls2))
