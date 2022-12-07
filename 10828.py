from sys import stdin

input = stdin.readline

n = int(input())

a_list = [input().split() for _ in range(n)]

stack_list = []

for i in a_list:
    
    if len(i) == 2:
        integer = int(i[1])
        
        stack_list.append(integer)
        
    else:
        command = i[0]

        if command == 'top':

            if len(stack_list) < 1:
                print(-1)
            else:
                print(stack_list[-1])

        elif command == 'size':
            print(len(stack_list))
        elif command =='empty':
            if stack_list:
                print(0)
            else:
                print(1)
        elif command =='pop':
            if len(stack_list) < 1:
                print(-1)
            else:
                pop_out = stack_list[-1]
                print(pop_out)
                del stack_list[-1]

    
