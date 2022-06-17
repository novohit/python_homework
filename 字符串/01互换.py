# TODO
n=int(input())
s=bin(n)[2:]
k=''
for i in s:
    k+=str(1-int(i))
print('{}:{}'.format(n,s))
print('{}:{}'.format(int(k,2),k))