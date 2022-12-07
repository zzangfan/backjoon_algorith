n = input()
alphabet_upper = [chr(i) for i in range(65,91,1)]
alphabet_lower = [chr(i) for i in range(97,123,1)]

result = ''
riot13 = 13
uppder_diff = ord('Z') - ord('A') + 1
lower_diff = ord('z') - ord('a') + 1
for i in n:
    if i  in alphabet_upper:
        if ord(i) + riot13 > 90:
            result += chr(ord(i) + riot13 - uppder_diff)

        else:
            result += chr(ord(i) + riot13)

    elif i in alphabet_lower:
        if ord(i) +riot13 > 122:
            result += chr(ord(i) + riot13 - lower_diff)

            
        else:
            result += chr(ord(i) + riot13)
            
    else:
        result += i
print(result)
    
