from collections import deque
from distutils.sysconfig import get_makefile_filename


n = int(input())
graph = [[] for _ in range(n)] 
answer = []
max_value = -9999
for i in range(n):
    a,b = map(int,input().split())
    graph[i] = (a,b)


def dfs(day):
    global max_value
    if day <= n:
        max_value = max(max_value,sum(answer))
       
    for i in range(day,n):
        
        t,p = graph[i]
        answer.append(p)
        dfs(i+t)
        answer.pop()

dfs(0)
print(max_value)
        