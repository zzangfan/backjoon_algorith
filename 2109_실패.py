n = int(input())
moneys = [list(map(int,input().split())) for _ in range(n)]

moneys.sort(key = lambda x:x[1])
moneys.sort(key = lambda x:x[0],reverse=True)


temp_day = 0
total = 0
for i in range(n):
    
    p,d = moneys[i]
    if d > temp_day:
        total += p
        temp_day += 1

print(total)