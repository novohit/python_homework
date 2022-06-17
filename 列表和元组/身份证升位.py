old = input()

year = int(old[6:8])
if year > 5:
    yn = '19'
else :
    yn = '20'

new = old[:6] + yn + old[6:]
w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]

s = 0
for i in range(len(new)):
    s += int(new[i]) * w[i]
mod = s % 11

x = '10X98765432'

print(new + x[mod])
