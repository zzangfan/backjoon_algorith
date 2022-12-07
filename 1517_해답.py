import sys

def mergesort(start:int,end:int) -> int:

    global cnt,arr
    
    if start < end:
        mid = (start + end) // 2
        mergesort(start,mid)
        mergesort(mid + 1, end)

        front_idx, back_idx = start, mid +1
        new_arr = []

        while front_idx <= mid and back_idx <= end:
            if arr[front_idx] <= arr[back_idx]:
                new_arr.append(arr[front_idx])
                front_idx += 1
            else:
                new_arr.append(arr[back_idx])
                back_idx += 1
                cnt +=  mid - front_idx + 1

        if front_idx <= mid:
            new_arr = new_arr + arr[front_idx : mid + 1]
        
        if back_idx <= end:
            new_arr = new_arr + arr[back_idx: end +1]

        for i in range(len(new_arr)):
            arr[start + i] = new_arr[i]


input = sys.stdin.readline
cnt = 0
n = int(input())
arr = [int(i) for i in input().split()]
mergesort(0,n-1)
print(cnt)