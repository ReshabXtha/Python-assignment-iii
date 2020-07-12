def merge_sort(lis1):
    if len(lis1) > 1:
        mid = len(lis1) // 2
        L = lis1[:mid]
        R = lis1[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                lis1[k] = L[i]
                i += 1
            else:
                lis1[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            lis1[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            lis1[k] = R[j]
            j += 1
            k += 1


lis1 = [2, 5, 6, 9, 7, 1, 3, 8]
merge_sort(lis1)
print(lis1)
