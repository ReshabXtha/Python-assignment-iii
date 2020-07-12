def part(lis1, low, high):
    pivot = lis1[high]
    i = low - 1
    for j in range(low, high):
        if lis1[j] <= pivot:
            i += 1
            lis1[i], lis1[j] = lis1[j], lis1[i]
    lis1[i + 1], lis1[high] = lis1[high], lis1[i + 1]
    return i + 1


def quick_sort(lis1, low, high):
    if low < high:
        p = part(lis1, low, high)
        quick_sort(lis1, low, p - 1)
        quick_sort(lis1, p + 1, high)


lis1 = [2, 5, 6, 9, 7, 1, 3]
quick_sort(lis1, 0, len(lis1) - 1)
print(lis1)
