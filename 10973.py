n = int(input())
nums = [int(i) for i in input().split()]
flag = False

for i in range(n-1,0,-1):
    if nums[i - 1] > nums[i]:
        for j in range(n-1,0,-1):
            if nums[i - 1] > nums[j]:
                nums[i - 1],nums[j] = nums[j] ,nums[i - 1]
                nums = nums[:i] + sorted(nums[i:],reverse=True)
                flag =True
                break

    if flag:
        print(*nums)
        break
if not flag:
    print(-1)