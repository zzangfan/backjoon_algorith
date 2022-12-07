N,K = [int(i) for i in input().split()]
a_list = []
count = 0

for i in range(N):
    a_list.append(int(input()))

for i in reversed(a_list):

    if K//i == 0:
        continue
    else:
        n = K//i
        count += n
        K -= n*i
print(count)