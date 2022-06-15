str = input()
letter = 0
digit = 0
other = 0
for c in str:
    if c.isalpha():
        letter += 1
    elif c.isdigit():
        digit += 1
    else:
        other += 1
print(f'letter = {letter}, digit = {digit}, other = {other}')