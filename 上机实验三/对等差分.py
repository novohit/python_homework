jh1 = set(map(int, input().split()))
jh2 = set(map(int, input().split()))
jh3 = jh1 ^ jh2
for x in jh3:
    print(x)