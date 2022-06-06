def sum(str):
    odd = 0
    even = 0
    for c in str:
        if int(c) & 1 == 1:
            odd += int(c)
        else:
            even += int(c)
    return odd, even

str = input()
odd, even = sum(str)
print('oddsum={},evensum={}'.format(odd, even))