def menu():
    print('''\n欢迎使用PYTHON学生通讯录
1：添加学生
2：删除学生
3：修改学生信息
4：搜索学生
5：显示全部学生信息
6：退出并保存''')
    n = int(input())
    if n == 2:
        name = input()
        delete(name)
    else:
        print("ERROR")
    print(dic)

def delete(name):
    if dic.get(name) != None:
        dic.pop(name)
        print("Success")
    else:
        print("No Record")

dic={'张自强': ['12652141777', '材料'], '庚同硕': ['14388240417', '自动化'], '王岩': ['11277291473', '文法']}
print(dic)
menu()