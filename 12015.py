import sys
from bisect import bisect_left

n = int(input())
arr = [int(i) for i in input().split()]
stack =[0]

for a in arr:
    if stack[-1] < a:
        stack.append(a)
    else:
        print(stack)
        print(bisect_left(stack,a))
        stack[bisect_left(stack,a)] = a


print(len(stack) -1)
