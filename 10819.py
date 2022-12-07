from itertools import permutations

n = int(input())
arr = [int(i) for i in input().split()]

permu = list(permutations(arr,n))

def cal(li):
    total = 0
    for i in range(len(li)-1):
        total += abs(li[i] - li[i+1])
    
    return total

answer = -1e9
for li in permu:
    answer = max(answer,cal(li))

print(answer)