def question_judge(question):
    """接收一个字符串为参数，根据参数值判断问题类型，调用合适的函数进行操作。"""
    if question == '素数':       # 如果输入”素数“，再输入一个正整数n，输出不大于n的所有素数
        n = int(input())
        output_prime(n)         # 输出素数
    elif question == '回文素数':
        n = int(input())
        palindromic_prime(n)   # 输出回文素数
    elif question == '反素数':
        n = int(input())
        reverse_prime(n)  # 输出反素数
    elif question == '哥德巴赫猜想':
        n = int(input())
        goldbach_conjecture(n)
    else:
        print('输入错误')



def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i <= n / i:
        if n % i == 0:
            return False
        i += 1
    return True


#输入一个正整数n，按从小到大顺序输出不大于n的所有素数。
def output_prime(number):
    for i in range(0, number + 1):
        if is_prime(i):
            print(i, end=' ')



def palindromic(num):
    """接收一个数字为参数，判定其是否为回文数，返回布尔值。"""
    return str(num) == str(num)[::-1]


def palindromic_prime(number):
    for i in range(0, number):
        # 要先判断回文 否则会超时 
        if palindromic(i) and is_prime(i):
            print(i, end=' ')



def reverse_num(num):
    """接收一个整数，返回其逆序字符串对应的整数"""
    return int(str(num)[::-1])


def reverse_prime(number):
    # 严格小于
    for i in range(0, number):
        #反素数指某数i及其逆序数都是素数，但数i对应的字符串不是回文字符串
        # 要先判断回文 否则会超时 
        if not palindromic(i) and is_prime(i) and is_prime(reverse_num(i)) :
            print(i, end=' ')

def goldbach_conjecture(num):
    if num < 4 or (num & 1) == 1:
        print('Data error!')
        return
    for i in range(2, num):
        if is_prime(i) and is_prime(num - i) and i <= (num - i):
            print(str(num) + '=' + str(i) + '+' + str(num - i))





if __name__ == '__main__':
    problems = input()
    question_judge(problems)