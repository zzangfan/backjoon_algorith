import sys
input = sys.stdin.readline
n = int(input())

a_list = []
answer = []
for i in range(n):
    command = input().split()

    if command[0] == 'push':
        a_list.append(command[1])
        
    elif command[0] == 'pop':
        if len(a_list) == 0 :
            answer.append(-1)
        else:
            answer.append(a_list[0])
            del a_list[0]
    elif command[0] =='size':
        answer.append(len(a_list))
    elif command[0] =='empty':
        if len(a_list) == 0:
            answer.append(1)
        else:
            answer.append(0)
    elif command[0] == 'front':
        if len(a_list) == 0:
            answer.append(-1)
        else:
            answer.append(a_list[0])

    elif command[0] =='back':
        if len(a_list) == 0:
            answer.append(-1)
        else:
            answer.append(a_list[-1])

for i in answer:
    print(i)