from collections import deque

n,m = map(int,input().split())

def dfs(x,mal,sum,minus,divide):
    print(x)
    if x <= m:
        answer = ""
        answer += "*" * mal
        answer += "+" * sum
        answer += "-" * minus
        answer += "/" * divide
        return print(answer)
    if x > m:
        return

    dfs(x**2,mal+1,sum,minus,divide)
    dfs(x+x,mal,sum+1,minus,divide)
    dfs(x-x,mal,sum,minus+1,divide)
    if x !=0:
        dfs(x/x,mal,sum,minus,divide+1)

print(dfs(n,0,0,0,0))



        


    