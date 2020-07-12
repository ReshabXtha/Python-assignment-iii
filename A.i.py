def toh(n, from_rod, to_rod, third):
    if n == 1:
        print("Move disk 1 from", from_rod, "to", to_rod)
        return
    toh(n - 1, from_rod, third, to_rod)
    print("Move disk", n, "from", from_rod, "to", to_rod)
    toh(n - 1, third, to_rod, from_rod)


toh(3, 'A', 'C', 'B')
