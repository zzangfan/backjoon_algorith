import re

Input = input().split()
if len(Input) >= 2:
    for i in Input:
        pass
else:
    Input = Input[0]
    pattern = re.compile("[^<][a-z0-9]*[^>]")
    m = pattern.search(Input)
    print(m)
        

