def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(i, n):
            if arr[j] < arr[i]:
                arr[j], arr[i] = arr[i], arr[j]
    return arr



array = [1, 353, 45, 1524, 1, 7, 8, 9, 495]

print(bubble_sort(array))
