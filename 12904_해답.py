start = list(input().rstrip())
answer = list(input().rstrip())

flag = False
while answer:
    if answer[-1] == 'A':
        answer.pop()
    elif answer[-1] == 'B':
        answer.pop()
        answer.reverse()
    
    if start == answer:
        flag = True
        break

print(1 if flag else 0)