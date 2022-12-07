import sys
input = sys.stdin.readline

n = int(input())
a_list = [int(i) for i in input().split()]
cnt = [0]
rest = [-1] * n
for i in range(1,n):
    
    while cnt and a_list[cnt[-1]] < a_list[i]:
        rest[cnt.pop()] = a_list[i]
    
    cnt.append(i)

print(*rest)