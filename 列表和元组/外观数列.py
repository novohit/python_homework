a, n = map(int, input().split(','))

def func(a, n):
        pre = ''
        cur = str(a)
        for _ in range(1, n):
            pre = cur
            cur = ''
            l = 0
            r = 0 # 循环不变量[l, r)
            # 统计前一项的信息
            while r < len(pre):
                # 统计重复元素的次数
                while r < len(pre) and pre[l] == pre[r]:
                    r += 1
                # 元素出现次数与元素进行拼接
                cur += str(r-l) + pre[l]
                # 继续统计下一个元素
                l = r
        return cur
print(func(a, n))