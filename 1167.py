from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    temp_graph = list(map(int,input().split()))
    index = 1
    while index != len(temp_graph) - 1:
        graph[temp_graph[0]].append([temp_graph[index],temp_graph[index+1]])
        index += 2

def bfs(start):
    que = deque()
    que.append([start,0])
    max_dis = 0 
    visited = [False] * (n+1)
    max_index = start
    visited[start] = True
    while que:
        now_index,now_distance = que.popleft()
        if max_dis < now_distance:
            max_dis = now_distance
            max_index = now_index
        
        for e, d in graph[now_index]:
            if not visited[e]:
                que.append([e,now_distance + d])
                visited[e] = True
    
    return max_index,max_dis

t_index,t_max = bfs(1)
final_index,final_max = bfs(t_index)
print(final_max)
    