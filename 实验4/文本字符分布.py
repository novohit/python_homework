map = dict()
with open("data.txt","r") as data:
    for line in data:
        for c in line:
            map[c] = map.get(c,0) + 1
    keys = sorted(map) # 字典排序返回列表
    for key in keys:
        print(key +':'+ str(map[key]))