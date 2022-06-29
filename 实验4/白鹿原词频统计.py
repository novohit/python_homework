import jieba 
f=open('白鹿原.txt','r',encoding='utf-8').read()
words=jieba.lcut(f)
counts={}
for word in words:
    if len(word)==1:
        continue
    else:
        counts[word]=counts.get(word,0)+1
items=list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
print(items[0][0])