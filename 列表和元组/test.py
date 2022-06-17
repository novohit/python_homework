tupa = (1, 2, 3, 4, 5)
tupb = ('aa', 2)
tupc = ('aaa', (1, 2, 3), [33, 44])
print(tupa, tupb, tupc)

tup1 = 1,
print(tup1)
t1 = tuple(range(1, 5))
print(t1)
t2 = tuple('hello')
print(t2)

t = tuple(range(10))
print(t)
print(t[::3])
ls1 = list()
print(ls1)
ls1.append('hello')
print(ls1)
ls2 = ['world']
ls2.extend(ls1)
print(ls2)
ls2.insert(0, 'a')
print(ls2)

# ls.pop(index) 返回被移除的元素  ls.pop()无参时 删除列表最后一个元素
# ls.remove(val) 删除列表中第一个与参数“x” 值相同的元素存在多个与x” 值相同元素时，只删除第一个
#del ls1 # 删除列表对象 del ls1[:]是删除列表全部元素
print(ls1)
ls1.sort(key = len)
ls1.sort(key = str.lower)

city = ['上海', '北京', '深圳']
order_city0 = enumerate(city) 
'''
给可遍历对象每个值增加一个序号
返回生成器，
可迭代对象
start
参数默认值为 0
'''
print(list(order_city0))
print(list(enumerate(city, 1)))

nums = [23, 1, 3, -3, 0, 7, -8, -9]
nums.sort(key= lambda x : (2, x) if x > 0 else (1, -x))
print(nums)