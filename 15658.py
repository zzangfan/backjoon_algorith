import sys
sys.setrecursionlimit(100000)

n = int(input())
nums = [int(i) for i in input().split()]
oper = [int(i) for i in input().split()]
max_value = -(sys.maxsize)
min_value = sys.maxsize
def dfs(idx,total,add,minus,multiply,divide):
    global max_value
    global min_value
    if idx ==n:

        max_value = max(total,max_value)
        min_value = min(total,min_value)
        return
        

    if add:
        dfs(idx+1,total + nums[idx],add -1,minus,multiply,divide)

    if multiply:
        dfs(idx+1,total * nums[idx],add,minus,multiply-1,divide)

    if minus:
        dfs(idx+1,total - nums[idx],add,minus-1,multiply,divide)
    if divide:
        dfs(idx+1,int(total/nums[idx]),add,minus,multiply,divide-1)
    
    

dfs(1,nums[0],oper[0],oper[1],oper[2],oper[3])
print(max_value)
print(min_value)