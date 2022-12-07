n = int(input())


def stars(number):

    if number == 1:
        return ['*']
    startList = stars(number//3)

    arr = []

    for i in startList:
        arr.append(i*3)
    for i in startList:
        arr.append(i +' ' * (number//3) + i)
    
    for i in startList:
        arr.append(i*3)

    return arr

print("\n".join(stars(n)))