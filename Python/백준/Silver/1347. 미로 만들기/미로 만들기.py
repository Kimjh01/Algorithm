import sys 

input = sys.stdin.readline

n = int(input())
arr = list(input().strip())

dir = 3 
x, y = 0, 0 

min_x, max_x = 0, 0
min_y, max_y = 0, 0
cor = [(0, 0)]

for now in arr:
    if now == 'F':
        if dir == 1: 
            y -= 1
        elif dir == 2: 
            x += 1
        elif dir == 3:
            y += 1
        elif dir == 4: 
            x -= 1
        
        cor.append((x, y))
        min_x, max_x = min(min_x, x), max(max_x, x)
        min_y, max_y = min(min_y, y), max(max_y, y)
        
    elif now == 'R':
        dir = dir + 1 if dir < 4 else 1
    elif now == 'L':
        dir = dir - 1 if dir > 1 else 4

w = max_x - min_x + 1
h = max_y - min_y + 1

mapping = [['#' for _ in range(w)] for _ in range(h)]

for cx, cy in cor:
    mapping[cy - min_y][cx - min_x] = '.'

for row in mapping:
    print("".join(row))