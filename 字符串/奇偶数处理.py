list1, list2 = [], []
while True:
    n = input()
    if n == '':
        break
    if int(n) % 2 == 0:
        list1.append(n)
    else:
        list2.append(n)
for i in list1[:-1]:
    print(i, end="-")
print(list1[-1])

for j in list2[:-1]:
    print(j, end="+")
print(list2[-1])

