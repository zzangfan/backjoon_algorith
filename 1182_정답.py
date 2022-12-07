n,m = map(int,input().split())
nums = [int(i) for i in input().split()]

count = 0
answer = []
def back_tracking(index,sum):
    global  count 
    
       
    if index >= n:
        return
    sum += nums[index]
    if sum == m:
        count +=1

    back_tracking(index + 1, sum -nums[index])
    back_tracking(index + 1, sum)

           
back_tracking(0,0)
print(count)
