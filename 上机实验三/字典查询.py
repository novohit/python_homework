dict1 = {'赵广辉':'13299887777','特朗普':'814666888','普京':'522888666','吴京':'13999887777'}
name = input()
if dict1.get(name) != None:
    print(name + ":" + dict1.get(name))
else:
    print("数据不存在")