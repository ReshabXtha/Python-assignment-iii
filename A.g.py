def into_search(l1, key):
    r = 0
    h = len(arr) - 1
    while r <= h and l1[r] <= key <= l1[h]:
        po = r + int(((float(h - r) / (l1[h] - l1[r])) * (key - l1[r])))
        if l1[po] == key:
            print(True)
            break
        elif l1[po] < key:
            r = po + 1
        else:
            h = po - 1


arr = [2, 3, 4, 10, 40, 5, 85]
x = 85
into_search(arr, x)
