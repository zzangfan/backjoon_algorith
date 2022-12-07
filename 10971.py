n = int(input())

arr = [[int(i) for i in input().split()] for _ in range(n)]
min_value = 1e9

def back_tracking(start,next,value,visited):
    global min_value

    if len(visited) == n:
        if arr[next][start] !=0:
            min_value = min(min_value, value + arr[next][start])
        return
    
    for i in range(n):

        if arr[next][i] !=0  and i not in visited and value < min_value:
            visited.append(i)
            back_tracking(start,i,value+arr[next][i],visited)
            visited.pop()


for i in range(n):
    back_tracking(i,i,0,[i])

print(min_value)