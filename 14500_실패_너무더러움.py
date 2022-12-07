N,M = map(int,input().split())
a_list = [[int(i) for i in input().split()] for _ in range(N)]

#함수를 만들어 접근을 할려고 했지만 너무나 많은 함수를 만들어야 하기 때문에 힌트를 찾은 결과 더 쉽고 빠르게 짜는 방법을 찾음

def one_poli(list,N,M):
    
    max_value = 0
    for i in range(N):
        for j in range(M-4):

            max_value = max(max_value,sum(a_list[i][j:j+4]))
    
    for i in range(N-4):
        for j in range(M):
            max_value = max(max_value,sum(a_list[i:i+4][j]))

    return max_value

def four_rect_poli(list,N,M):
    max_value = 0
    for i in range(N-2):
        for j in range(M-2):
            total = 0 
           
            total += sum(a_list[i][j:j+2])
            total += sum(a_list[i+1][j:j+2])
            max_value = max(max_value,total)
    return max_value

def L_poli(list,N,M):
    max_value = 0
    for i in range(N-3):
        for j in range(M-2):
            total = 0
            total += sum(a_list[i][j])
            total += sum(a_list[i+1][j])
            total += sum(a_list[i+2][j:j+2])

            max_value = max(max_value,total)

    for i in range(N-3):
        for j in range(M-2):
            total = 0
            total += sum(a_list[i][j+1])
            total += sum(a_list[i+1][j+1])
            total += sum(a_list[i+2][j:j+2])
            
            max_value = max(max_value,total)
    
    for i in range(N-2):
        for j in range(M-3):
            total = 0
            total += sum(a_list[i][j+2])
            total += sum(a_list[i+1][j:j+3])

            max_value = max(max_value,total)

    for i in range(N-2):
        for j in range(M-3):
            total = 0
            

    
    return max_value
    


