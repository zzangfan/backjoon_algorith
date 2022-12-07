import sys
input = sys.stdin.readline

n = int(input())
a_list = [int(i) for i in input().split()]
answer = []
flag = False
for i in range(n):
    number = a_list[i]
    for j in a_list[i+1:]:
        if j > number:
            answer.append(j)
            flag = True
            break
        else:
            pass
    if flag == False:
        answer.append(-1)
    else:
        flag = False
print(" ".join(map(str,answer)))