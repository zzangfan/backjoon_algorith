from itertools import combinations
n,m = map(int, input().split())
answer = combinations([i for i in range(1,n+1)],m)

for i in answer:
    print(' '.join(map(str,i)))