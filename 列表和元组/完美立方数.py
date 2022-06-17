n = int(input())

for i in range(1, n + 1):
    for j in range(2, n + 1):
        for k in range(j, n + 1):
            for l in range(k, n + 1):
                if i**3 == j**3 + k**3 + l**3:
                    print("Cube = {},Triple = ({},{},{})".format(i,j,k,l))

