n = int(input())
graph = [list(input()) for _ in range(n)]

def revese(x,y,kind='row'):
    global graph
    if kind == "row":

        for i in range(x,x+n):
            value = graph[i][y]
            if value == 'H':
                graph[i][y] = 'T'
            else:
                graph[i][y] = 'H'
    elif kind == "col":
        for i in range(y,y +n):
            value = graph[x][i]
            if value == 'H':
                graph[x][i] = 'T'
            else:
                graph[x][i] = 'H'

print(graph)
revese(0,0)
print(graph)
        