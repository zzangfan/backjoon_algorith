import sys,heapq

N,K = map(int,input().split())
graph = [list(map(int,input().split())) for _ in range(N)]
bags = [int(input()) for _ in range(K)]
graph.sort()
bags.sort()
tmp = []
result = 0
for bag in bags:
    while graph and bag > graph[0][0]:
        heapq.heappush(tmp,-graph[0][1])
        print(graph)
        heapq.heappop(graph)
        print(graph)
  
    if tmp:
        result += heapq.heappop(tmp)
    elif not graph:
        break

print(result)