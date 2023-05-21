a = [1, 2, 4, 5, 7, 12, 23, 4, 3, 13]
def bubble_sort(array):
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] < a[j]:
                a[i], a[j] = a[j], a[i]
    return a

def QuickSort(B):
    if len(B) <= 1:
        return B
    else:
        c = B[0]
        D = []
        E = []
        F = []
        for elem in A:
            if elem < c:
                L.append(elem)
            elif elem > c:
                R.append(elem)
            else:
                M.append(elem)
        return QuickSort(D) + E + QuickSort(F)

print(QuickSort(a))





