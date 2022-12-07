
def dfs(idx,depth):
        if depth == 6:
            print(*total)
            return
        
        for i in range(idx,n):
            
            total.append(lotto[i])
            dfs(i+1,depth+1)
            total.pop()

while True:
    nums= [int(i) for i in input().split()]
    
    n = nums[0]
    total = []
    if n == 0:
        exit()
    lotto = sorted(nums[1:].copy())
    
    dfs(0,0)
    print()
    

