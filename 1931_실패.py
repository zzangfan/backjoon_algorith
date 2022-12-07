N = int(input())
a_list = []

for i in range(N):
    a_list.append([int(i) for i in input().split()])

count = 0
number = 0

count_list = 0

for hall_number in range(N):
    
    int_start = hall_number
    check_list = []
    for i in range(N):
        temp_start,_ = a_list[i]
        if int_start == temp_start:
            check_list.append(i)
    if len(check_list) == 0:
        continue
    min_value = 2**31 - 1
    exist = False
    for j in check_list:
        _,end = a_list[j]

        check_number =0
        for k in a_list:
            
            check_start, check_end = k
            if (end+1) == check_start:
                value = check_end - check_start

                if min_value >  value:
                    min_value = value
                    
                    number = check_number + 1
                    exist = True
            check_number += 1
    
    if exist == False:
        continue
    else:

        count += 1

   
    

   

        
print(count)
        
        
            
        

    


