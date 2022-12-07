n = int(input())
a_list = []
for _ in range(11):
    a_list.append(list(map(int,input().split())))

a_list.sort(key=lambda x: x[0])
a_list.sort(key=lambda x: x[1])

cnt = 1
end = a_list[0][1]
for i in range(1,n):
    if a_list[i][0] >= end:
        cnt += 1
        end = a_list[i][1]

print(cnt)