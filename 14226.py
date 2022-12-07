from collections import deque


n = int(input())


def bfs(start):

    
    que = deque()
    que.append(start)
    count = 1
    while que:
