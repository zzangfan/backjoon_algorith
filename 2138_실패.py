import sys
sys.setrecursionlimit(100000)
n = int(input())
input_list = [int(i) for i in input().rstrip()] 
answer_list = [int(i) for i in input().rstrip()]

d = (-1,0,1)

answer = []
def dfs(x,list,cnt):
    
    if x ==n:
        if list == answer_list:

       
            answer.append(cnt)
        
        return 
     
    
    temp_list = list
    for dx in d:
        nx = x + dx

        if nx < 0 or nx >= n:
            continue
        
        if list[nx] == 1:
            list[nx] = 0
        else:
            list[nx] = 1
    
    dfs(x+1,list,cnt+1)
    
    dfs(x+1,temp_list,cnt)
    
dfs(0,input_list,1)
if answer:
    print(min(answer))
else:
    print(-1)
