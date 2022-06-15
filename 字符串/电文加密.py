import string

n = input()
lower = string.ascii_lowercase
upper = string.ascii_uppercase
s1 = lower + upper
s2 = lower[::-1] + upper[::-1]
table=''.maketrans(s1,s2)
print(n.translate(table))
