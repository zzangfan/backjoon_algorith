import sys
input = sys.stdin.readline
n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))

arr.sort(key = lambda x:(x[1],x[0]))
for i in arr:
    print(*i)