def check_eval(x,y,op):
    if op == '<':
        if x > y : return False
    if op == '>':
        if x < y : return False
    return True

def back_dfs(index,num):
    if index == n + 1:
        answer.append(num)
        return

    for i in range(10):
        if visited[i]: continue
    
        if index == 0  or check_eval(num[index-1],str(i),operators[index-1]):
            visited[i] = True
            back_dfs(index +1, num+str(i))
            visited[i] = False





n = int(input())
operators = input().split()
visited= [False] * 10
answer = []

back_dfs(0,'')
answer.sort()

print(answer[-1])
print(answer[0])