import sys
NUM,CHAR = 10, 26
input = sys.stdin.readline

total = 1
strings = list(input().strip())
for idx,i in enumerate(strings):
    if idx ==0 or strings[idx-1] !=i:
        total *= NUM if i =='d' else CHAR
    else:
        total *=  (NUM -1) if i =='d' else (CHAR-1)

print(total)



