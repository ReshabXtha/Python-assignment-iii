def bin_search(l1, l, r, x):
    if l <= r:
        mid = l + (r - l) // 2
        if l1[mid] == x:
            print(True)

        elif l1[mid] < x:
            return bin_search(l1, mid + 1, r, x)
        else:
            return bin_search(l1, l, mid - 1, x)
    else:
        print(False)


arr = [2, 3, 4, 10, 40, 5, 85]
x = 40
bin_search(arr, 0, len(arr) - 1, x)
