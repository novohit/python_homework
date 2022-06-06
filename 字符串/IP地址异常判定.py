def func(str):
    ls = str.split('.')
    for i in range(len(ls)):
        if ls[i].isdigit() and int(ls[i]) <= 255 and int(ls[i]) >= 0:
            continue
        else:
            print('No')
            return
    print('Yes')
    
str = input()
func(str)