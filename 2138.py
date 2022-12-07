n = int(input())
bulb = list(map(int,input()))
target = list(map(int,input()))

def change(A,B):
    L = A[:]
    presse = 0
    for i in range(1,n):

        if L[i-1] == B[i-1]:
            continue
        
        press += 1
        for j in range(i-1,i+2):
            if j < n:
                L[j] = 1 - L[j]

    return press if L == B else 1e9

res = change(bulb,target)

bulb[0] = 1 - bulb[0]
bulb[1] = 1 - bulb[1]

res = min(res,change(bulb,target)+1)
print(res if res != 1e9 else -1)