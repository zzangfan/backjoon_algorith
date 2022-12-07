from sys import stdin
input = stdin.readline

Input = input()
flag = 0
Input = Input.replace("()","1")
answer = 0

for i in Input:
    if i == "(":
        flag += 1
        answer += 1

    elif i ==")":
        flag -= 1
    else:
        answer += flag

    

print(answer)
        
        


