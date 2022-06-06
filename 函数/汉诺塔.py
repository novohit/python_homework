def hanno(n, source, target, help):
    if n == 1:
        print(source ,'-->', target)
        return
    hanno(n - 1, source, help, target)
    print(source ,'-->', target)
    hanno(n - 1, help, target, source)

n = eval(input())
a, b, c = input().split()
hanno(n, a, c, b)