# bubble Sort
def bob_sort(lis1):
    for i in range(len(lis1)):
        for j in range(len(lis1) - i - 1):
            print(j)
            if lis1[j] > lis1[j + 1]:
                lis1[j], lis1[j + 1] = lis1[j + 1], lis1[j]


lis1 = [2, 5, 6, 9, 7, 1, 3]
bob_sort(lis1)
print(lis1)
