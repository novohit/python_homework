def DataMasking():
    mask = [input().split() for i in range(n)]
    for item in mask:
        item[0] = item[0][:4] +  '*' * 7 + item[0][11:]
        item[1] = item[1][0] + '*' + item[1][2:]
        item[2] = item[2][:3] + '*' * 4 + item[2][7:]
    return mask

if __name__ == '__main__':
    n = int(input())
    print('ERROR') if n <= 0 else print(DataMasking())