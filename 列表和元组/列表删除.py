str = '我有一所房子面朝大海春暖花开'
ls = list(str)

m, n = map(int, input().split(','))
del ls[m:n]
print(ls)