n = list(input())
n.sort(reverse=True)
print(n)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or "0" not in n:
    print(-1)
else:
    print("".join(n))