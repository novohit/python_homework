from cgitb import reset
import jieba
print(jieba.lcut('理想的书籍是智慧的钥匙'))
def fact(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

def fun(name, city = 'shanghai', hobby = 'running'):
    return f'my name is {name} and come from {city} like {hobby}'

# 包裹传递
def func1(*name):
    print(name) # 一个元组：('hello', 'world', '!')


# 两个* 包裹可以传递map key-value值
def func2(**name):
    print(name) # 一个字典：{'a': 'hello', 'b': 'world', 'c': '!'}

def func3(name, age):
    print(name, age)


ans = fact(6)
print(ans)
print(fun(name='beijing'))
func1('hello', 'world', '!')
func2(a = 'hello', b = 'world', c = '!')


person = ('zwx', 18)
func3(*person) # 解包裹传递 可以理解为传递了person指针

person = {'name':'tom', 'age':11}
func3(**person)

# 匿名函数
ls = [-5, -9, 6, 10, 8]
print(sorted(ls))

print(sorted(ls, key=lambda x:x**2))