import sys

left = list(input())
right = []
M = int(input())

for i in range(M):
    command = sys.stdin.readline().split()

    if command[0] =='L':
        if left:
            right.append(left.pop())
    elif command[0] == 'D':
        if right:
            left.append(right.pop())
    elif command[0] == 'B':
        if left:
            left.pop()
    elif command[0] =='P':
        left.append(command[1])

right.reverse()
for i in left+right:
    print(i,end='')