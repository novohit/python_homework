freqDict = eval(input())
ls = input().split()
for x in ls:
    if freqDict.get(x) != None:
        freqDict[x] += 1
    else:
        freqDict.setdefault(x, 1)
print(freqDict)