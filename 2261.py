import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    x,y = list(map(int,input().split()))
    arr.append((x,y))
arr.sort()

def get_dist(a,b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

def dac(start,end):
    if start == end:
        return float('inf')

    if end - start == 1:
        return get_dist(arr[start],arr[end])
    
    mid = (start+end)//2
    minDist = min(dac(start,mid),dac(mid,end))

    target_pl = []
    #x축
    for i in range(start,end+1):
        if (arr[mid][0] -arr[i][0]) ** 2 < minDist:
            target_pl.append(arr[i])
    
    target_pl.sort(key=lambda x: x[1])

    t = len(target_pl)
    #y축
    for i in range(t-1):
        for j in range(i+1,t):
            if  (target_pl[i][1] - target_pl[j][1])**2 < minDist:
                minDist = min(minDist, get_dist(target_pl[i],target_pl[j]))
            else:
                break
    
    return minDist

print(dac(0,n-1))