str = input()
i = int(input())
ls = ['2', '3', '0', '1', '5']
if i >= 5:
    ls.extend([str, str])
else:
    ls.insert(i, str)
    ls.append(str)
print(ls)
