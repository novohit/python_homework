import string

password = input()

def getnum(password):
    count = 0
    digflag, lowflag, upflag, otherflag = 0, 0, 0, 0
    for c in password:
        if digflag == 0 and c in string.digits:
            count += 1
            digflag = 1
        elif lowflag == 0 and c in string.ascii_lowercase:
            count += 1
            lowflag = 1
        elif upflag == 0 and c in string.ascii_uppercase:
            count += 1
            upflag = 1
        elif otherflag == 0 and c in string.punctuation:
            count += 1
            otherflag = 1
    return count

def func(password):
    if len(password) < 8:
        print('弱')
        return
    count = getnum(password)
    if count == 1:
        print('弱')
        return
    if count == 4:
        print('极强')
    elif count == 3:
        print('强')
    elif count == 2:
        print('中')

func(password)