start = input()
answer = input()
word_len = len(answer)

while len(start) < word_len:
    start = start + 'A'
    if start == answer:
        print(1)
        exit()
    else:
        start = start[::-1] + 'B'
        
        if start == answer:
            print(1)
            exit()

print(0)