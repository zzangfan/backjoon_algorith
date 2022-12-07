n = int(input())

answer = []
deck = []

for i in range(n):
    command = input().split()

    if command[0] =='push_front':
        temp_deck = [command[1]]
        deck = temp_deck + deck
        
    elif command[0] =='push_back':
        deck.append(str(command[1]))
    elif command[0] =='pop_front':
        if len(deck) == 0:
            answer.append('-1')
        else:
            pop_out = deck[0]
            del deck[0]
            answer.append(pop_out)
    elif command[0] =='pop_back':
        if len(deck) == 0:
            answer.append('-1')
        else:
            pop_out = deck[-1]
            del deck[-1]
            answer.append(pop_out)
    elif command[0] =='size':
        answer.append(len(deck))
    elif command[0] =='empty':
        if len(deck) == 0:
            answer.append('1')
        else:
            answer.append('0')
    elif command[0] =='front':
        if len(deck) == 0:
            answer.append('-1')
        else:
            answer.append(deck[0])
    elif command[0] =='back':
        if len(deck) == 0:
            answer.append(-1)
        else:
            answer.append(deck[-1])
for i in answer:
    print(i)