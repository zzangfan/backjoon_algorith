import sys

input = sys.stdin.readline
n =int(input())
answer = set()

for i in range(n):
    command = input().split()
    
    if len(command) == 1:
       
        if command[0] == "all":
            answer = set([i for i in range(1,21)])
        
        else: 
            answer.clear()
        continue
    
    
    command, num = command[0] , int(command[1])
        
       
    if command == "add":
        answer.add(num)
    elif command == "remove":
        answer.discard(num)
    elif command == "check":
        if num in answer:
            print(1)
        else:
            print(0)
    elif command == "toggle":
        if num in answer:
            answer.discard(num)
        else:
            answer.add(num)

   
