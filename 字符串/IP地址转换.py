ip_address = input()                            # 输入合法的ip地址
for c in ip_address:                            # 遍历输入的字符串
	if c not in '01' or len(ip_address) != 32:  # 若其中有字符不是'0'或'1'，或是字符串长度不是32
		print('data error!')                    # 输出'data error!'
		break                                   # 结束程序
else:                                           # 遍历正常结束时执行此分支下的语句
	ip_string = str(int(ip_address[0: 8], 2))   # 将前8个字符取出转为整数字符串，作为IP地址的第一部分
	for i in range(1, 4):                       # 遍历3次，将后面24个字符转为整数再转字符串拼接在字符串上
		ip_string = ip_string + '.' + str(int(ip_address[i * 8:(i + 1) * 8], 2))
	print(ip_string)                            # IP合法时，输出转换为十进制的IP地址

# 借助列表和集合可简化程序
ip_address = input()                                                         # 输入合法的ip地址
if len(ip_address) != 32 or set(ip_address) != {'0', '1'}:                   # 若其中有字符不是'0'或'1'，或是字符串长度不是32
	print('data error!')                                                     # 输出'data error!'
else:
	ip_lst = [str(int(ip_address[i * 8:(i + 1) * 8], 2)) for i in range(4)]  # 每8位二进制转为一个十进制整数，放入列表中
	print('.'.join(ip_lst))                                                  # 用点'.'拼接列表中的字符串为IP地址
# 推荐写法
def ip_test(ip_address):
    """
    >>> ip = '11111111111111111111111111111111'
    >>> ip_test(ip)
    '255.255.255.255'
    >>> ip = '11001100100101000001010101110010'
    >>> ip_test(ip)
    '204.148.21.114'
    """
    if len(ip_address) == 32 and set(ip_address) <= {'0', '1'}:
        return '.'.join([str(int(ip_address[i * 8:(i + 1) * 8], 2)) for i in range(4)])
    else:
        return 'data error!'


if __name__ == '__main__':
    ip = input()
    print(ip_test(ip))