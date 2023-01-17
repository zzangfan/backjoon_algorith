import sys

input = sys.stdin.readline

menu = [int(i) for i in input().split()]
Y,H,B = menu[:3]
YN,HN = menu[3:]

max_count = max(HN,YN)
min_count = min(HN,YN)
total = 0
if B * (min_count*2) <= H * (min_count) + Y * (min_count):
    total += B * (min_count*2)

    HN -= min_count
    YN -= min_count

    if HN > 0 and HN * H > B * HN * 2:
        total += (B*HN*2)
    else:
        total += HN * H

    if YN > 0 and YN * Y > B * YN * 2:
        total += (Y*YN*2)
    else:
        total += YN * Y

    if B * (max_count*2) < total:
        print(B * (max_count*2))
        exit()
    else:
        print(total)
        exit()




else:


    total += H * HN
    total += Y * YN
    print(total)
    exit()