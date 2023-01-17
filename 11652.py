import sys

input = sys.stdin.readline
n = int(input())
card = {}

for i in range(n):
    a = int(input())
    if a in card:
        card[a] += 1
    else:
        card[a] = 1

result = sorted(card.items(),key = lambda x: (-x[1],x[0]))
print(card.items())
print(result[0][0])



