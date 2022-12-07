import itertools
n = input()
nums = len(n) + 1
string_n = list(n)

n = int(n)
thirty = set()

value = 30
count = 1

while value * count < 10 ** nums:
    thirty.add(value * count)
    count += 1

answer = []
for i in range(1,nums):
    for j in itertools.permutations(string_n,i):
        value = int("".join(j))
        answer.append(value)
    
answer.sort(reverse=True)

for i in answer:
    if i in thirty:
        print(i)
        exit()
print(-1)


