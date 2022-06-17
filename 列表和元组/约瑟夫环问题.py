def func(n,k):
    ls = list(range(1,n+1))
    index = 0
    while True:
        temp = ls.pop(0)
        index += 1
        if index == k:
            index = 0
            continue
        ls.append(temp)
        if len(ls)==k-1:
            print(sorted(ls,reverse=False))
            break

def main():
    n,k = map(int,input().split())
    if k < 2 or n < k:
        print("Data Error!")
        return
    func(n,k)
    
main()
