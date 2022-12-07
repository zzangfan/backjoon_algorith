import sys
input = sys.stdin.readline
first_str = (input()).replace("\n","")

n = int(input())
cur = len(first_str) 
for i in range(n):
    command = input().split()
    if len(command) == 2:
        
        if cur == 0:

            first_str = command[1] + first_str
           
            cur += 1
        elif cur  == len(first_str):
            first_str = first_str + command[1]
            
            cur +=1
        else:
            first_str = first_str[:cur] + command[1] + first_str[cur:]
           
            cur +=1
    else:

        if command[0] == "L":
            if cur == 0:
                pass
            else:
                cur -=1
            
        elif command[0] =="D":
            if cur ==  len(first_str):
                pass
            else:
                cur +=1
        elif command[0] == "B":
            if cur == len(first_str):
                first_str = first_str[:cur-1]
                
                cur -=1
            elif cur == 0:
                pass
            
            else:
                first_str = first_str[:cur-1] + first_str[cur:]
                
                cur -=1
            
print(first_str)