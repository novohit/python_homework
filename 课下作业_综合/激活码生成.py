import random
n = int(input())
random.seed(n)

def func():
    for i in range(5):
        key = ""
        for j in range(10):
            choice = random.randint(1, 5)
            if choice == 1:
                key += str(random.randint(0,9))
            elif choice == 3 or choice == 2:
                key += chr(random.randint(ord('A'),ord('Z')))
            elif choice == 4 or choice == 5:
                key += chr(random.randint(ord('a'),ord('z')))
        print(key)

func()
