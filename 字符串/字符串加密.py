str = input()
# ord('L')：将字符转换成ascii码 chr(42):反之
res = ''
for i in range(len(str)):
    # python的字符串是一种不可变对象(immutabel object)，意味着只读不写，线程安全 要修改字符串只能新建一个或者先转成list再转回来
    if 'a' <= str[i] <= 'z':
        res += chr((ord(str[i]) - ord('a') + 3 ) % 26 + ord('a'))
    elif 'A' <= str[i] <= 'Z':
        res += chr((ord(str[i]) - ord('A') + 5 ) % 26 + ord('A'))
    else:
        res += str[i]
print(res)