from collections import deque

def bfs():
    global map
    que = deque()
    que.append([7,0])
    turn = 0
   
    while que:
        len_q = len(que)
        for _ in range(len_q):
            row, col = que.popleft()

            if map[row][col] == '#':
                continue
            
            if (row,col) == (0,7):
                return 1

            for dx,dy in d:
                nx = row + dx
                ny = row + dy

                if nx <0  or nx >=8  or ny <0  or ny >= 8:
                    continue
            
                if map[nx][ny] =='.':
                    que.append((nx,ny))
        
        map.pop()

        map.appendleft(['.','.','.','.','.','.','.','.'])

        turn += 1

        if turn == 9:
            return 1
    return 0



map = deque(list(input()) for _ in range(8))
d = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1),(0,0)]

print(bfs())