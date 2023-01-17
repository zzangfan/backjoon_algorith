n = int(input())
arr =[list(map(int,input().split())) for _ in range(n)]
arr.sort(key = lambda x: (x[0],x[1]))
print((arr[0][0] - arr[1][0])**2 + ((arr[0][1]) - arr[1][1])**2)
