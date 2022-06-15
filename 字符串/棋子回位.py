str = input()
dong = 0
xi = 0
nan = 0
bei = 0

for c in str:
    if c == '东': dong += 1
    elif c == '西': xi += 1
    elif c == '南': nan += 1
    else : bei += 1

if dong == xi and nan == bei:
    print('是')
else:
    print('否')