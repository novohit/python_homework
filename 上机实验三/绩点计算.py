rank = 0
all_rate = 0
dic = {'A':4.0,'A-':3.7,'B+':3.3,'B':3.0,'B-':2.7,'C+':2.3,'C':2.0,'C-':1.5,'D':1.3,'D-':1.0,'F':0}
 
while s := input():
    if s == '-1':
        break
     
    rate = int(input())
    all_rate += rate
    rank += dic[s] * rate
 
print(f'{rank/all_rate:.2f}')