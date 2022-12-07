N = int(input())
a_list = [[int(i) for i in input().split()] for _ in range(N)]
answer = []
for M,N,x,y in a_list:
    count = 1
    temp_x = 1
    temp_y = 1
    flag = False
    for i in range(10001):
        count +=1
        if temp_x < M:
            temp_x +=1
        elif temp_x >= M:
            temp_x = 1
        
        if temp_y < N:
             temp_y +=1
        elif temp_y >= N:
            temp_y = 1

        if x == temp_x and y == temp_y:
            flag = True
            answer.append(count)
            break

    if flag == False:
        answer.append(-1)
for i in answer:
    print(i)

