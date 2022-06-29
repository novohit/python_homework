import numpy as np

def readfile(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        score = file.read().replace('\n', ',').split(',')   # 前面三行可以用这一行实现
    return score                                            # 返回列表

def arrayshape(score):                                      # score 为传入的列表
    scoreArray = np.array(score).reshape(6, 8)                  # 前面两行可以用这一行实现
    return scoreArray                                       # 返回仅包含成绩的整数数组

def studentInfo(studentName):
    scoreNum = scoreArray[1:, 2:].astype(int)               # 数组scoreArray切片，将成绩部分转为整数
    indexStudent = np.argwhere(scoreArray == studentName)   # 返回学生所有位置，如[[4,0]]
    studentRow = indexStudent[0,0]                          # 返回学生所在的行序号，如4
    meanStudent = np.mean(scoreNum[studentRow - 1])         # 计算学生平均成绩
    return indexStudent,round(meanStudent,2)

def courseInfo(courseName):
    scoreNum = scoreArray[1:, 2:].astype(int)                # 数组scoreArray切片，将成绩部分转为整数
    indexcourse = np.argwhere(scoreArray == courseName)      # 返回课程所有位置，如[[0,4]]
    courseColumn = indexcourse[0, 1]                         # 返回课程所在的列序号，如4
    meancourse = np.mean(scoreNum[0:, courseColumn - 2])     # 计算课程平均成绩
    mediancourse = np.median(scoreNum[0:, courseColumn - 2]) # 计算课程成绩中位数
    stdcourse = np.std(scoreNum[0:, courseColumn - 2])       # 计算成绩标准差
    return indexcourse,round(meancourse,2),round(mediancourse,2),round(stdcourse,2)

if __name__ == '__main__':
    filename = '成绩单数字.csv'                               # 读取的文件名
    score = readfile(filename)                               # 调函数读文件，返回列表
    scoreArray = arrayshape(score)                           # 列表转数组
    studentName = input()                                    # 输入学生姓名
    student = studentInfo(studentName)                       # 调用函数，返回学生序号和学生平均成绩
    print(f'{student[0]}')        # 输出学生位置序号
    print(f'{studentName}',end='')
    print('同学的平均成绩为{:0.2f}'.format(student[1]))
    
    courseName = input()                                     # 输入课程名
    course = courseInfo(courseName)                          # 调用函数统计课程成绩，返回课程序号，平均分，中位数和标准差
    print(f'{course[0]}')             # 输出课程位置序号
    print(f'{courseName}课程平均成绩为', end='')             # 输出课程平均成绩
    print('{:0.2f}'.format(course[1]))
    print('该课程中位数为{:0.2f}'.format(course[2]))
    print('该课程标准差为{:0.2f}'.format(course[3]))