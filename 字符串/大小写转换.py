import string
str = input()
#print(string.ascii_lowercase)#abcdefghijklmnopqrstuvwxyz
for c in str:
    if c in string.ascii_lowercase:
        print(c.upper(),end='')
    elif c in string.ascii_uppercase:
        print(c.lower(),end='')
    else:
        print(c,end='')