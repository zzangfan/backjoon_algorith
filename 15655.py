n,m = [int(i) for i in input().split()]
numbers = [int(i) for i in input().split()]
numbers.sort()
answer = []
def back_dfs(depth):

    if depth == m:
        print(*answer)
        return

    for i in range(depth,n):
        if numbers[i] not in answer:
            answer.append(numbers[i])
            back_dfs(depth+1)
            answer.pop()
back_dfs(0)
