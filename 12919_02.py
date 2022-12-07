input_string = list(input().rstrip())
answer_string = list(input().rstrip())

while answer_string:
    if answer_string[-1] == 'A':
        answer_string.pop()
    elif answer_string[-1] == 'B':
        answer_string.pop()
        answer_string = answer_string[::-1]
       
    
    if answer_string == input_string:
        
        print(1)
        exit()
print(0)
