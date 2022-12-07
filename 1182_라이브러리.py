from itertools import combinations
n,m = map(int,input().split())
nums = [int(i) for i in input().split()]

count = 0
answer = []

for i in range(1,n+1):
    com = combinations(nums,i)
   
    for j in com:
        
        if sum(j) == m:
            count +=1
            continue
print(count)