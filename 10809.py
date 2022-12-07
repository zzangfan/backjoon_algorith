import sys

input = sys.stdin.readline
a_list = list(input().strip())

first_number = ord('a')
alpha_cnt =  [-1 for i in range(26)]

for index,i in enumerate(a_list):
    
    if  alpha_cnt[ord(i) - first_number] == -1:
        alpha_cnt[ord(i) - first_number] = index
    else:
        pass

print(*alpha_cnt)
