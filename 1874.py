n = int(input())
stack = []
answer = []
flag = 0
cur = 1
for i in range(n):
    number = int(input())
    while cur <= number :
        stack.append(cur)
        answer.append("+")
        cur +=1

    if stack[-1] == number:
        stack.pop()
        answer.append("-")
    else:
        print("NO")
        flag = 1
        break
if flag == 0:
    for i in answer:
        print(i)