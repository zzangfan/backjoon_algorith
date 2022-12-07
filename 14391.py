n,m = map(int,input().split())
nums = [[int(i) for i in list(input())] for _ in range(n)]

def back_tracking(depth,index):

    if 