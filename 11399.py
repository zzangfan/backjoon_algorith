n = int(input())
a_list = [int(i) for i in input().split()]
a_list.sort()
total = 0
wait_time = 0

for i in a_list:
    wait_time += i
    
    total += wait_time
print(total)
