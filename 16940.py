from collections import deque


n = int(input())
graph = [[] for i in range(n+1)]
cycle = n - 1
for _ in range(cycle):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
answer = [int(i) for i in input().split()]
visited = [-1] * (n+1)
children = [set() for _ in range(n+1)]
def bfs(start):

    que = deque()
    que.append(start)
   
    visited[start] = 0
    while que:
        now = que.popleft()

        for i in graph[now]:
            if visited[i] == -1:
                visited[i] = visited[now] + 1
                children[now].add(i)
                que.append(i)
               
                visited[i] = True
next_index = 1
for i in answer:
    if next_index == n:
        break
    c_len = len(children[i])
    c1 = set(answer[next_index:next_index+c_len])
    c2 =children[i]
    if c1 != c2:
        print(0)
        exit()
    next_index += c_len
print(1)



    
