def average(array):
    # 你的代码写在这里
    jh = set(array)
    return round(sum(jh)/len(jh), 3)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)