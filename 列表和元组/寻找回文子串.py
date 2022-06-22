str = input()
res = []
for i in range(len(str) - 1, 1, -1):
    for j in range(0, len(str) - 1 - i + 1):
        sub_str=str[j:j + i]
        if sub_str == sub_str[::-1]:
            res.append(sub_str)
if len(res) == 0:
    for c in str:
        res.append(c)
res.sort()    
print(res)

'''
# 区间dp
def func(str):
    ls = []
    n = len(str)
    if n < 2:
        ls.append(str)
        return ls
    dp = [[0] * n] * n

    # 长度为1都为回文串
    for i in range(n):
        dp[i][i] = True
    
    max_len = 1
    # 枚举区间长度
    for i in range(1, n + 1):
        # 枚举左边界
        for j in range(n + 1):
            if j + i - 1 < n:
                l, r = j, j + i - 1
                if str[l] != str[r]:
                    dp[l][r] = False
                else:
                    # 如果两端相等且长度小于等于3必为回文串
                    if r - l + 1 <= 3:
                        dp[l][r] = True
                    else:
                        # 如果两端相等 等于上一个状态 因为可能出现某段是回文串但两端不是，整体就不是
                        dp[l][r] = dp[l + 1][r - 1]

                if dp[l][r] and r - l + 1 >= max_len:
                    max_len = r - l + 1
                    ls.append(str[l:r + 1])
    res = []
    for x in ls:
        if len(x) == max_len:
            res.append(x)
    print(sorted(res))

func(str)
'''