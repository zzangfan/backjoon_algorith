n,m = map(int,input().split())
nums = [int(i) for i in input().split()]

answer = 0
def dfs(idx,sum):
    global answer
    
    if idx >= n:
        return
    
    sum += nums[idx]
    if sum == m:
        answer +=1
       
    

    dfs(idx+1,sum - nums[idx])
    dfs(idx + 1,sum)
dfs(0,0)
print(answer)