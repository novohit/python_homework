str = input()
big = 0
small = 0
num = 0
sp = 0
other = 0
for c in str:
    if 'A' <= c <= 'Z': big += 1
    elif 'a' <= c <= 'z': small += 1
    elif '0' <= c <= '9': num += 1
    elif c == ' ': sp += 1
    else: other += 1
print(small, big, num, sp, other)