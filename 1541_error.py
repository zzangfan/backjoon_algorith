Input = input().replace("\n","")
if "-" in Input:

    A_list = Input.split("-")
    if "+" in A_list[0]:
        init_number = sum([int(i) for i in A_list[0].split("+")])
    else:
        init_number = int(A_list[0])
    B_list = A_list[1:]
    total_list = []
    for i in B_list:
        total = 0
    
        for j in [int(k) for k in i.split("+") if len(k) !=0]:
            total += j
        total_list.append(total)
    answer = 0
    for i in total_list:
        answer += int(i)
    print(init_number - answer)
else:
    total =sum([int(i) for i in Input.split("+") if len(i) !=0])
    
    print(total)


            