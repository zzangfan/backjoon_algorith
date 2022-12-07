import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline

n = int(input())
balls = [int(i) for i in input().split()]
max_value = -sys.maxsize

def dfs(sum):
    global max_value
    if len(balls) == 2:
        max_value = max(max_value,sum)
        return

    for i in range(1,len(balls)-1):
        temp_sum = balls[i - 1] * balls[i + 1]

        v = balls.pop(i)
        dfs(sum + temp_sum)
        balls.insert(i,v)

dfs(0)
print(max_value)