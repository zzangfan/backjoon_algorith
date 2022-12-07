n,m = map(int,input().split())
nums = [int(i) for i in input().split()]

count = 0
answer = []
def back_tracking(index):
    global  count 
    if len(answer) > 0:
       
        if sum(answer) == m:
           
            count +=1

    for i in range(index,n):
        if nums[i] not in answer:
            answer.append(nums[i])
            back_tracking(index+i)
           
            answer.pop()
           
back_tracking(0)
print(count)
