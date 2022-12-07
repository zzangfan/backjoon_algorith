import heapq
import sys

input = sys.stdin.readline

n = int(input())
lectures = [list(map(int,input().split())) for _ in range(n)]

lectures.sort(key = lambda x:x[1])
print(lectures)
que = []

for p,d in lectures:
    heapq.heappush(que,p)

    if d < len(que):
        heapq.heappop(que)
    
print(sum(que))