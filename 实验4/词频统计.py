import string


def read_file(file):
    """接收文件名为参数，将文件中的内容读为字符串，
    只保留文件中的英文字母和西文符号，
    过滤掉中文(中文字符及全角符号Unicode编码都大于256)
    将所有字符转为小写，
    将其中所有标点、符号替换为空格，返回字符串
    """
    with open(file, 'r', encoding='utf-8') as novel:
        txt = novel.read()
    english_only_txt = ''.join(x for x in txt if ord(x) < 256)
    english_only_txt = english_only_txt.lower()
    for character in string.punctuation:
        english_only_txt = english_only_txt.replace(character, ' ')
    return english_only_txt



def count_of_words(txt):
    """接收去除标点、符号的字符串，统计并返回其中单词数量和不重复的单词数量"""
    words_list = txt.split()
    amount_of_words = len(txt.split())
    amount_of_words_no_repeat = len(set(words_list))
    return amount_of_words, amount_of_words_no_repeat



def word_frequency(txt):
    """接收去除标点、符号的字符串，统计并返回每个单词出现的次数
    返回值为字典类型，单词为键，对应出现的次数为值"""
    frequency = dict()
    words_list = txt.split()
    for word in words_list:
        frequency[word] = frequency.get(word, 0) + 1
    return frequency



def top_ten_words(frequency, cnt):
    """接收词频字典，输出出现次数最多的cnt个单词及其出现次数"""
    frequency_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for word, counts in frequency_items[:cnt]:
        print(word, counts)



def top_ten_words_no_excludes(frequency, cnt):
    """接收词频字典，去除常见的冠词、代词、系动词和连接词后，输出出现次数最多的
    cnt个单词及其出现次数，需排除的单词如下：
    excludes_words = ['a', 'an', 'the', 'i', 'he', 'she', 'his', 'my', 'we',
    'or', 'is', 'was', 'do', 'and', 'at', 'to', 'of', 'it', 'on', 'that', 'her',
    'c','in', 'you', 'had','s', 'with', 'for', 't', 'but', 'as', 'not', 'they', 
    'be', 'were', 'so', 'our','all', 'would', 'if', 'him', 'from', 'no', 'me', 
    'could', 'when', 'there','them', 'about', 'this', 'their', 'up', 'been', 
    'by', 'out', 'did', 'have']
    """
    excludes_words = ['a', 'an', 'the', 'i', 'he', 'she', 'his', 'my', 'we',
                      'or', 'is', 'was', 'do', 'and', 'at', 'to', 'of', 'it', 
                      'on', 'that', 'her', 'c','in', 'you', 'had','s', 'with', 
                      'for', 't', 'but', 'as', 'not', 'they', 'be', 'were', 
                      'so', 'our','all', 'would', 'if', 'him', 'from', 'no',
                      'me', 'could', 'when', 'there','them', 'about', 'this', 
                      'their', 'up', 'been', 'by', 'out', 'did', 'have']
    for word in excludes_words:
        frequency.pop(word)
    frequency_items = sorted(frequency.items(), key=lambda x: x[1], reverse=True)
    for word, counts in frequency_items[:cnt]:
        print(word, counts)



# 取消这段和代码最后二行注释可以绘制词云，仅供参考
def draw_cloud(frequency):
    """绘制词云，传入参数为词频，设定图片的宽度600，高度400，背景白色、字体最大值150、图片边缘为5。"""
    wc = WordCloud(max_words=80,              # 设置显示高频单词数量
                  width=600,                 # 设置图片的宽度
                  height=400,                # 设置图片的高度
                  background_color='White',  # 设置背景颜色
                  max_font_size=150,         # 设置字体最大值
                  margin=5,                  # 设置图片的边缘
                  scale=1.5)                 # 按照比例进行放大画布，如设置为1.5，则长和宽都是原来画布的1.5倍。
    wc.generate_from_frequencies(frequency)   # 根据文本内容直接生成词云
    plt.imshow(wc)                            # 负责对图像进行处理，并显示其格式，但是不能显示。
    plt.axis("off")                           # 不显示坐标轴
    wc.to_file('My Cheese.png')               # 词云保存为图片
    plt.show()                                # 显示图像



if __name__ == '__main__':
    filename = 'Who Moved My Cheese.txt'  # 文件名
    content = read_file(filename)  # 调用函数返回字典类型的数据
    frequency_result = word_frequency(content)  # 统计词频
    cmd = input()
    if cmd == '1':
        n = int(input())
        print(content[:n])
    elif cmd == '2':
        amount_results = count_of_words(content)
        print('文章共有单词{}个，其中不重复单词{}个'.format(*amount_results))
    elif cmd == '3':
        n = int(input())
        top_ten_words(frequency_result, n)
    elif cmd == '4':
        n = int(input())
        top_ten_words_no_excludes(frequency_result, n)
        # frequency_no_excludes = top_ten_words_no_excludes(frequency_result)
        # draw_cloud(frequency_no_excludes)