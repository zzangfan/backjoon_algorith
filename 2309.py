

a_list = []
answer = []
total = 100
for _ in range(9):
    a_list.append(int(input()))
a_list.sort()
for i in range(9):
    for j in range(i,9):
        if sum(a_list) - (a_list[i] + a_list[j]) == 100:
            m = [a_list[i],a_list[j]]
            break
a_list.remove(m[0])
a_list.remove(m[1])

print('\n'.join(map(str,sorted(a_list))))