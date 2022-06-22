
def lucky_boy(total, mum):
    # 约瑟夫环问题
    ls = list(range(0,total))
    index = 0
    while True:
        temp = ls.pop(0)
        index += 1
        if index == mum:
            index = 0
            continue
        ls.append(temp)
        if len(ls) == mum - 1:
            print(sorted(ls,reverse = False))
            break

if __name__ == '__main__':
    total, mum = map(int, input().split())
    if mum < 2 or mum > total:
        print("Data Error!")
    else:
        lucky_boy(total, mum)
