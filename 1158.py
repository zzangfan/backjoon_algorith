import sys
input = sys.stdin.readline
N, K = [int(i) for i in input().split()]
circle = [i + 1 for i in range(N)]

index = K - 1
answer = []
while circle :
   
    number = circle.pop(index)
    answer.append(str(number))
    
    index += K - 1
    
    if index >= len(circle) and len(circle) !=0:
       
        index %= len(circle) 
       
    else:
        pass
print("<",", ".join(answer),">",sep="")
