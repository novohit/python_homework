def func(str, numRows):
    if (numRows == 1):
        return str
    res = ""
    s_len = len(str)
    num = numRows * 2 - 2
    for row in range(numRows):
        col = 0
        while row + col < s_len:
            res += str[row + col]
            if (row != 0 and row != numRows - 1 and col + num - row < s_len):
                res += str[col + num - row]
            col += num
    return res

str = input()
n = int(input())
print(func(str, n))
