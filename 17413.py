import re
a_list = input().split()
answer = []
position = []
end = 0
for i in a_list:
    string = ""
    pattern = re.compile("<{1}[a-z0-9 ]*>{1}")
    m = pattern.finditer(i)
    
    if m:

        for j in m:
        
            position.append(j.span())
            
        
        end_list = []
        
        for k in position:

            if len(end_list) != 0:
                start = k[0]
                end = k[1]
                
                if len(i) > end:
                    string += i[]
                else:

                    last_end = end_list[-1]
                    reverse_string = i[last_end:start]
                    reverse_string = reverse_string[::-1]
                    string += reverse_string
                    string += i[start:end]
                    
                    
                    end_list.append(end)
            else:
            
                start = k[0]
                end = k[1]
                
                string += i[start:end]
            
                end_list.append(end)
        answer.append(string)
   
        
  
print(answer)
