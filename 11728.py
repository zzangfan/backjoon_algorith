import sys
input = sys.stdin.readline
n,m= map(int,input().split())
answer = list(map(int,input().split()))
answer.extend(map(int,input().split()))

answer.sort()
for i in answer:
    print(i,end=' ')