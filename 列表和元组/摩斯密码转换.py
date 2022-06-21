import string
ls = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.", "---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

str = input()
for i in range(len(str)):
    if str[i].isalpha():
        temp = str[i].lower()
        print(ls[ord(temp) - ord('a')],end='')
    else:
        print(str[i],end='')