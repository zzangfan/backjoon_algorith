


n = int(input())
a_list = [i for i in input().split()]

min_value = float('inf')
max_value = float('-inf')

answer = []
def back_dfs(depth):
    global min_value,max_value
    if depth == n + 1:
        count = 0
        first_number = answer[0]
        for sign,number in zip(a_list,answer[1:]):
            if eval('{}{}{}'.format(first_number,sign,number)):
               
                first_number = number
                count +=1
            else:
                break
                
        if count == n:
            combination_number = int(''.join(map(str,answer)))
            min_value = min(min_value,combination_number)
            max_value = max(max_value,combination_number)
          
            return

        
    for i in range(10):
        if i not in answer:
            
            answer.append(i)
            back_dfs(depth+1)
            answer.pop()

back_dfs(0)
print(str(max_value).zfill(n+1))
print(str(min_value).zfill(n+1))
