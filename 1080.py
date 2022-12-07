n,m = map(int,input().split())
input_list = [list(map(int,input()))for _ in range(n)]
answer_list = [list(map(int,input()))for _ in range(n)]

def check():
    for i in range(n):
        for j in range(m):
            if input_list[i][j] != answer_list[i][j]:
                return False

    return True

count = 0
for i in range(n-2):
    
    for j in range(m-2):
        
        temp_count = 0
        for ni in range(i,i+3):
            for nj in range(j,j+3):
               
                if input_list[ni][nj] != answer_list[ni][nj]:
                    
                    temp_count +=1
        
        if temp_count !=0:
          
       
            for ni in range(i,i+3):
                for nj in range(j,j+3):
                    
                
                    input_list[ni][nj] = 1 - input_list[ni][nj]
        
            count += 1

            if check():
            
                print(count)
                exit()

print(-1)