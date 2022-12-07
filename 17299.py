import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
a_list = [int(i) for i in input().split()]
res = [-1] * n
stack = [0]
con = [0] *(1000001) #이게 문제였네

for i in a_list:
    con[i] += 1


for i in range(1,n):

    while stack and con[a_list[stack[-1]]] < con[a_list[i]]:
        res[stack.pop()] = a_list[i]
        
        
    stack.append(i)

print(*res)