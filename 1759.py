n,m = map(int,input().split())

strings =[i for i in input().split()]
strings.sort()

check_co = ['a','e','i','o','u']
answer = []

def check(arr):

    mo = 0
    co = 0
    for i in range(n):
        if answer[i] in check_co:
            mo +=1
        else:
            co +=1
    
    if mo >= 1 and co >= 2:
        return True
    else:
        return False
       

def back_dfs(idx):

    if len(answer) is n:
        if check(answer) is False:
            return
        for i in answer:
            print(i,end='')
        print()
        return
    for i in range(idx,m):
        answer.append(strings[i])
        back_dfs(i+1)
        answer.pop()
 
back_dfs(0)