import sys

input = sys.stdin.readline

n = int(input())
nums = list(map(int,input().split()))
answer = set()

def back_tracking(idx,sum):

    if idx >=n:
        return

    sum += nums[idx]
    
    answer.add(sum)
    back_tracking(idx+1,sum)
    back_tracking(idx+1,sum - nums[idx])

back_tracking(0,0)
for i in range(1,max(answer)+1):
    if i not in answer:
        print(i)
        exit()

print(max(answer)+1)