import sys
sys.setrecursionlimit(10000000)
n = int(input())
inputs = [list(input()) for _ in range(n)]
charaters = [chr(ord('A') + i) for i in range(26)]
unique = {i:-1 for i in set().union(*inputs)}

max_value = -1

if len(unique) > 8:
    n = 8
else: n = len(unique)

def dfs(depth):
    global max_value
    global inputs
    if depth == n:
        
        value = 0
        for i in inputs:
           
            temp = ""
            
            for j in i:
                if unique[j] != -1:
                    temp += str(unique[j])
            if temp != '':
                value += int(temp)
            

        if max_value < value:
            max_value = value
            
        
        return
    for j in range(1,10):
        for i in unique.keys():
            if unique[i] == -1:
                unique[i] = j
                dfs(depth+1)
                unique[i] = -1

        
dfs(0)

print(max_value)