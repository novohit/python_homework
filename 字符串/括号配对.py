map = {'}': '{', ')': '(', ']': '['}
val, key = map.values(), map.keys()
 
 
def isValid(s):
    arr = []
    for c in s:
        if c in val:
            # 左括号入栈
            arr.append(c)
        elif c in key:
            # 右括号，要么栈顶元素出栈，要么匹配失败
            if arr and arr[-1] == map[c]:
                arr.pop()
            else:
                return False
    return True

print(isValid(input()))