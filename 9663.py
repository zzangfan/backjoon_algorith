import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
graph = [[]*n for _ in range(n)]


dx = [-1,1,0,0,1,-1,1,-1]
dy = [0,0,-1,1,1,-1,-1,1]

chess_loc = []


def dfs(idx,depth):

    if depth == n:
        
        print(*chess_loc)
        return

    for i in range(idx,n):
        for j in range(idx,n):
            if (i,j) not in chess_loc:
                chess_loc.append((i,j))
                dfs(idx+1,depth+1)
                chess_loc.pop()

dfs(0,0)

    
