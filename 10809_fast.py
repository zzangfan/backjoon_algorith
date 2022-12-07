string_list = list(input())
alphabet = [chr(i) for i in range(97,97+26,1)]
base = [-1 for i in range(len(alphabet))]
for idx,i in enumerate(string_list):
    
    for index,j in enumerate(alphabet):
        if i==j and base[index] == -1:
            base[index] = idx
            break
[print(i,end=" ") for i in base]