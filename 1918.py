a_list = input()
stack = []
ans = ''
for i in a_list:

    if "A" <= i <= "Z":
        ans += i
    else:
        if i == '(':
            stack.append(i)
            

        elif i == '*' or i =='/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                ans += stack.pop()
            stack.append(i)
            
        elif i =='+' or i =='-':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.append(i)

        elif i ==')':
            while stack and stack[-1] != '(':
                ans += stack.pop()
            stack.pop()
      
while stack:
    ans += stack.pop()

print(ans)