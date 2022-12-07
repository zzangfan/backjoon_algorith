from re import L


graph = [[] * 9 for _ in range(9)]

for i in range(9):
    inputs = list(map(int,input().split()))
    graph[i] = inputs


for i in range(3):
    for j in range(3):
        count = 0
        temp_number = [i for i in range(1,10)]
        temp_loc = []
        
        for rindex,row in enumerate(graph[i:(i+1)*3]):
            for colindex,col in enumerate(row[j:(j+1)*3]):
                
                if col == 0:
                    count += 1
                    print((i*3) + rindex,(j+3) + colindex)
                    temp_loc.append([(i*3) + rindex,(j+3) + colindex])
                    
                    continue
                if col in temp_number:
                    
                    temp_number.remove(col)
                    
                    continue
            
        if count == 1:
            print(temp_loc)
            graph[temp_loc[0],temp_loc[1]] = temp_number
                    

