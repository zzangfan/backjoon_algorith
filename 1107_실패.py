n = int(input())
m = int(input())
error_list = [int(i) for i in input().split()]
error_list.sort()
not_error_list = [i for i in range(0,10) if i not in error_list]

answer = 100
str_n = list(str(n))
count = 0

if n == 100:
    print(count)
else:

    answer = ""
    for i in str_n:
        if int(i) in error_list:
            min_value = 99999
            for k in not_error_list:
                min_value = min(int(i) - k,min_value)
            
            answer += str(int(i) - min_value)
            count +=1
        else:
            answer += i
            count += 1




    answer = int(answer)
    if answer == n:
        print(count)
    else:
        while True:
            if answer < n:
                count += 1
                answer += 1
            elif answer > n:
                count +=1
                answer -= 1
            
            if answer == n:
                break
        print(count)