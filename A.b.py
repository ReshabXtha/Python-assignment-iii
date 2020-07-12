# Insertion sort
def ins_sort(lis1):
    for i in range(1, len(lis1)):
        key = lis1[i]
        j = i - 1
        while j >= 0 and key < lis1[j]:
            lis1[j + 1] = lis1[j]
            j = j - 1
        lis1[j + 1] = key


lis1 = [2, 5, 6, 9, 7, 1, 3]
ins_sort(lis1)
print(lis1)
