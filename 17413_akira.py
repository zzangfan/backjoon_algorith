import sys
import re
input = sys.stdin.readline
Input = input()
def reverse(sentence):
    pattern = r"(?<=\b)[a-z0-9]*(?=\b)" #space find
    return re.sub(pattern, lambda x:x.group(0)[::-1],pattern.group(0))

pat = r"(?:^|(?<=>))[a-z0-9 ]*(?=$|<)" #tag find
#?: lookbehind 그룹에 들어가진 않음
#?= lookhead 그룹에 들어가진 않음
print(re.sub(pat,reverse,Input))

