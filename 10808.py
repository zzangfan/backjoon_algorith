import sys

input = sys.stdin.readline
a_list = input().strip()

first_number = ord('a')

alpha_cnt = [0] * 26
for i in a_list:

    alpha_cnt[ord(i) - first_number] += 1

print(*alpha_cnt)



