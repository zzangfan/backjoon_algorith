n = int(input())
a_list = []
for i in range(n):
    a_list.append(int(input()))

a_list.sort()
total_list = []
length = len(a_list)
divide_number = 1
for i in a_list:
    total = i*length
    total_list.append(total)
    length -= 1
   

print(int(max(total_list)))
