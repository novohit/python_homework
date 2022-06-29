with open('score.csv', 'r', encoding='utf-8') as csv_obj:
    ls = []
    for line in csv_obj:
        ls.append(line.strip().split(','))
print(ls)

