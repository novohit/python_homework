for i in range(1, 101):
    for j in range(1, 101):
        for k in range(1, 101):
            if (5 * i + 3 * j + k * 1 / 3) == 100 and (i + j + k == 100):
                print(i, j, k)