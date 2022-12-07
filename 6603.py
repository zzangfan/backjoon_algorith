
def back_tracking(depth,idx):
    
    if depth == 6:
        print(*answer)
        return 

    for i in range(idx,length):

        answer.append(nums[i])
        back_tracking(depth+1,i+1)
        answer.pop()

    

while True:
    
    temp = [int(i) for i in input().split()]
    length = temp[0]
    nums = sorted(temp[1:].copy())
    answer = []
    back_tracking(0,0)
    if length == 0:
        exit()
    print()
