#알파벳 소문자, 알파벳 대문자, 숫자, 공백
from string import ascii_lowercase, ascii_uppercase,whitespace

alpa_lower = list(ascii_lowercase)
alpa_upper = list(ascii_uppercase)
number = [str(i)for i in range(10)]
white = list(whitespace)



while True:
    try:
        inputs = input()
    except:
        break
    if not inputs:
        break

    answer = [0]* 4
    for j in inputs:
        if j in alpa_lower:
            answer[0] += 1
        elif j in alpa_upper:
            answer[1] += 1
        elif j in number:
            answer[2] += 1
        elif j in white:
            answer[3] += 1
        else:
            pass

    print(*answer)