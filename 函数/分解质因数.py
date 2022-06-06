# 提示：递归函数调用
def defactor(N):      # 定义一个函数名称为defactor，意义是返回N的所有因子
    for i in range(2, N):
        if N % i ==0: # 如果试到 i 是 N 的因子的话，就返回i的所有因子和N/i的所有因子 的列表
            return defactor(i) + defactor(int(N // i))
    else:             # 如果没有试到就说明这个N是一个质数，就直接包含它的 列表
        return [N]    # 返回列表
        
if __name__ == '__main__':
    n = int(input())
    print(defactor(n))