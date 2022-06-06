def F2C(f):
    return '{:.2f}'.format(5*(f-32)/9, 2)

def printTable(f1, f2):
    if f1 > f2:
        print('error')
        return
    for i in range(f1, f2 + 1, 2):
        print(i,':', F2C(i))

f1, f2 = input().split(',')
printTable(int(f1), int(f2))