

import sys
n = int(input())
nums = list(map(int,input().split()))

oper = list(map(int,input().split()))
lens = sum(oper)
max_value = -(sys.maxsize)
min_value = sys.maxsize

def dfs(depth,total,plus,minus,multiply,divide):
    global max_value, min_value
    if depth == n:
        max_value = max(total, max_value)
        min_value = min(total, min_value)

    if plus:
        dfs(depth + 1,total + nums[depth],plus - 1, minus,multiply,divide)
    if minus:
        dfs(depth + 1,total - nums[depth], plus, minus -1 ,multiply, divide)
    if multiply:
        dfs(depth + 1,total * nums[depth], plus, minus, multiply - 1, divide)

    if divide:
        dfs(depth + 1,int(total/nums[depth]),plus,minus,multiply,divide -1)

dfs(1,nums[0],oper[0],oper[1],oper[2],oper[3])
print(max_value)
print(min_value)