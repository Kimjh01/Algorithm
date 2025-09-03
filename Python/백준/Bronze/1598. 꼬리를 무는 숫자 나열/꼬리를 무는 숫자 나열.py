a, b = map(int, input().split())

ra, ca = (a-1) // 4, (a-1) % 4
rb, cb = (b-1) // 4, (b-1) % 4

print(abs(ra - rb) + abs(ca - cb))