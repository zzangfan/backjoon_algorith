n = int(input())

arr = []
for i in range(n):
    a,b = input().split()
    arr.append([int(a),b])

arr.sort(key = lambda x: x[0])
arr.sort(key = lambda x: x[1],reverse=True)
for i in arr:
    print(*i)
