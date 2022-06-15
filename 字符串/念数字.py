map = {
    '-':'fu',
    '0':'ling',
    '1':'yi',
    '2':'er',
    '3':'san',
    '4':'si',
    '5':'wu',
    '6':'liu',
    '7':'qi',
    '8':'ba',
    '9':'jiu'
    }
str = input()
for i in range(len(str)):
    if i != len(str) - 1:
        print(map[str[i]], end = ' ')
    else:
        print(map[str[i]])