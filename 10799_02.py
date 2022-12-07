import re

Input = input()

f_rods = re.sub(r"\(\)",".",Input)

r_rods = re.findall(r"(\(+|\)+|.)",f_rods)

curr = 0
total = 0

for i in r_rods:
    if i[0] == '(':
        curr +=len(i)
        total += len(i)
    elif i[0] ==')':
        curr -= len(i)
    else:
        total += curr*len(i)
print(total)

