squre = [[0] * 100 for _ in range(100)]
sum_area = 0

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            squre[i][j] = 1

for i in range(100):
    for j in range(100):
        if squre[i][j] == 1:
            sum_area += 1

print(sum_area)
