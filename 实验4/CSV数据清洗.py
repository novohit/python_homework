with open("data.csv","r") as obj:
    for line in obj:
        line = line.replace(" ", "")
        print(line, end="")