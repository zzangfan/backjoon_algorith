n = int(input())
s_set = set(int(i) for i in input().split())
m = int(input())
ss_list = [int(i) for i in input().split()]
answer = [1 if i in s_set else 0 for i in ss_list]
print(*answer)

