n,m = map(int,input().split())
a_list = []
count = 0

for i in range(n):
    a_list.append(int(input()))

for i in reversed(a_list):
    if m//i == 0 :
        continue
    else:
        n = m//i
        count += n
        m -= n*i
print(count)