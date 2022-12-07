n = int(input())
graph = [list(map(int,list(input()))) for _ in range(n)]

x_direction = [-1,1,0,0]
y_direction = [0,0,-1,1]

def dfs(x,y):
   

    if x<0 or x>=n or y<0 or y>=n:
        return False
    
    if graph[x][y] == 1:
        global count
        count +=1
        graph[x][y] = 0
    
        for i in range(4):
            temp_x = x +x_direction[i]
            temp_y = y + y_direction[i]
            
            dfs(temp_x,temp_y)
        return True
    return False


answer = []
count = 0
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            answer.append(count)
            result +=1
            count = 0
       
answer.sort()
print(result)
print("\n".join(map(str,answer)))
