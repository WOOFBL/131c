def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2] 
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot] 
    return quick_sort(left) + middle + quick_sort(right)

array = [1, 353, 45, 1524, 1, 7, 8, 9, 495]
print(quick_sort(array))
