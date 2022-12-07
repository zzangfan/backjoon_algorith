n = int(input())

str_list = [input().split() for _ in range(n)]

for i in str_list:
    answer = []
    for j in i:
        if len(j) == 1:
            answer.append(j)
        else:
            answer.append(j[::-1])

    print(' '.join(answer))