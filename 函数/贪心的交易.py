import random

# 动态规划
def f(prices):
    print(prices)
    if len(prices) == 0:
        return 0
    
    dp = [0] * 2
    dp[0] = 0
    dp[1] = -prices[0]
    pre0 = dp[0]
    for i in range(1, len(prices)):
        dp[0] = max(dp[0], dp[1] + prices[i]) #今天不持股的情况 之前也不持股或者今天卖出
        dp[1] = max(dp[1], pre0 - prices[i]) #今天持股的情况 之前就持股或者今天买入
        pre0 = dp[0]
    return dp[0]
'''
# 贪心
def f2(prices):
    print(prices)
    if len(prices) == 0:
        return 0
    res = 0
    for i in range(1, len(prices)):
        res += max(0, prices[i] - prices[i - 1])
    return res
'''

n = eval(input())
seed = eval(input())
random.seed(seed)
ls=[random.randint(1,100) for i in range(0,n)]   #构造价格列表，本行无需修改，
print(f(ls))               #输出结果，本行无需修改