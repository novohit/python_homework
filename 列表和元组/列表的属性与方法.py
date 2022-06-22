n = int(input())
ls = []
for i in range(n):
    command_ls = input().split()
    if command_ls[0] == 'insert':
        ls.insert(int(command_ls[1]), int(command_ls[2]))
    elif command_ls[0] == 'print':
        print(ls)
    elif command_ls[0] == 'remove':
        ls.remove(int(command_ls[1]))
    elif command_ls[0] == 'sort':
        ls.sort() # 原地排序
    elif command_ls[0] == 'append':
        ls.append(int(command_ls[1]))
    elif command_ls[0] == 'pop':
        ls.pop()
    elif command_ls[0] == 'reverse':
        ls.reverse()