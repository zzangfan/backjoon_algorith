

dic = {}

n = int(input())

for _ in range(n):

    word = input().rstrip()

    for i in range(len(word)):

        if word[i] in dic :
            dic[word[i]] += 10**(len(word) - (i+1))
        else:
            dic[word[i]] = 10**(len(word) - (i+1))

result = []

for value in dic.values():
    result.append(value)
result.sort(reverse=True)

sum = 0
num = 9
for value in result:
    sum += value * num
    num -= 1

print(sum)