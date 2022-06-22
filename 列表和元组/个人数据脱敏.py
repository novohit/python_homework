n = input()


def func(n):
    if n.isalnum() == False:
        print("ERROR")
        return
    n = int(n)
    map = []

    while n != 0:
        num, name, phone = input().split()
        new_num = num[0:4] + "*******" + num[11:]
        if len(name) == 2:
            new_name = name[0] + "*"
        else:
            new_name = name[0] + "*" + name[2:]
        new_phone = phone[0:3] + "****" + phone[7:]
        map.append([new_num, new_name, new_phone])
        n -= 1

    print(map)
func(n)