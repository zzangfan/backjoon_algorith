import sys
from collections import Counter
input = sys.stdin.readline
n = int(input())
a_list = [int(i) for i in input().split()]
res = [-1] * n
stack = [0]

con = Counter(a_list)



for i in range(1,n):

    while stack and con[a_list[stack[-1]]] < con[a_list[i]]:
        res[stack.pop()] = a_list[i]
        
        
    stack.append(i)

print(*res)