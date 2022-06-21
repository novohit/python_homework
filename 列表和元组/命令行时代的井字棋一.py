ls = eval(input())
for i in range(7):
    if i & 1 == 0:
        print("|-----|-----|-----|")
    elif i == 1:
        print(f"|  {ls[0]}  |  {ls[1]}  |  {ls[2]}  |")
    elif i == 3:
        print(f"|  {ls[3]}  |  {ls[4]}  |  {ls[5]}  |")
    elif i == 5:
        print(f"|  {ls[6]}  |  {ls[7]}  |  {ls[8]}  |")

