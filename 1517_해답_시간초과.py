def bubble_sort(arr):
    global cnt


    for i in range(n):
        for j in range(0,n - i - 1):
            if arr[j] > arr[j + 1]:
                cnt += 1
                arr[j],arr[j + 1] = arr[j + 1],arr[j]



cnt = 0
n = int(input())
arr = [int(i) for i in input().split()]
bubble_sort(arr)
print(cnt)


