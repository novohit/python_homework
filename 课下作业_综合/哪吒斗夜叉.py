# 枚举夜叉数量
for i in range(36):
    # 枚举哪吒数量
    for j in range(36):
        if i + j * 3 == 36 and i * 8 + j * 6 == 108:
            print(j, i)