ls = []

while s := input():
    if s == '':
        break
    ls.append(s.split())
ls.sort(key = lambda x : eval(x[1][:-1]) * 1000 if x[1][-1] == 't' else eval(x[1][:-2]))
print(ls)