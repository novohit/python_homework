import io

try:
    f = open('静夜诗.txt','r', encoding='utf-8')
    for line in f:
        print(line.strip())
    f.write('你好')
except io.UnsupportedOperation:
    print('缺失写权限')

finally:
    f.close()