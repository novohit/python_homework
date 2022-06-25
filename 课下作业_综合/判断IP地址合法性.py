str = input()

def isVaild(str):
    ls = str.split('.')
    if len(ls) != 4:
        return False
    for c in ls:
        if len(c) > 1 and c[0] == '0':
            return False
        if not c.isdigit():
            return False
        if int(c) < 0 or int(c) > 255:
            return False
    return True

if isVaild(str):
    print('Yes')
else:
    print('No')