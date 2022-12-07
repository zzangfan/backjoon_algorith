N = int(input())



A =[int(i) for i in input().split()]
B =[int(i) for i in input().split()]
A.sort(reverse=True)
B.sort(reverse=False)

total = 0

for a,b in zip(A,B):
    total += a*b

print(total)