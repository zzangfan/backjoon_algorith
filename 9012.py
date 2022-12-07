import sys
input = sys.stdin.readline
n = int(input())
a_list = []

for i in range(n):
    answer = input()
    sum = 0
    for j in list(answer):
        if j =='(':
            sum +=1
        elif j ==')':
            sum -= 1
        
        if sum < 0:
            a_list.append("NO")
            break
        
    
    if sum > 0 :
        a_list.append("NO")
    elif sum == 0 :
        a_list.append("YES")



print("\n".join(a_list))

