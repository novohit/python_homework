str = input()
L = 0
R = 0
B = 0

for i in range(len(str)):
    if str[i] == 'L': L += 1
    elif str[i] == 'R': R += 1
    elif str[i] == 'B': B += 1

res = (R - L + 2 * B) % 4

if res == 0:
    print('E')
elif res == 1:
    print('S')
elif res == 2:
    print('W')
elif res == 3:
    print('N')
