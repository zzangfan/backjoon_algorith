from collections import Counter
n = int(input())
s_set = [int(i) for i in input().split()]
s_set = Counter(s_set)


m = int(input())
ss_list = [int(i) for i in input().split()]
for i in ss_list:
    if i in s_set.keys():
        print(s_set[i],end = ' ')
    else:
        print(0,end=' ')

