f = open("sensor-data-1k.txt", "r")
all_sum, count = 0, 0
for line in f:
  ls = line.split()
  count += 1
  all_sum += eval(ls[4])
print("{:.2f}".format(all_sum / count))