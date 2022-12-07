from itertools import combinations, repeat

n,m = [int(i) for i in input().split()]
numbers = [int(i) for i in input().split()]
numbers.sort()
answer= []

def back_dfs(depth):

    if depth == m:
        print(" ".join(map(str,answer)))
        return
    
    for i in numbers:
        if i not in answer:
            answer.append(i)
            back_dfs(depth+1)
            answer.pop()

back_dfs(0)