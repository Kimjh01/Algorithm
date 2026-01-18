import sys

input = sys.stdin.readline
data = list(map(int, input().split()))

N = data[0]
A, B, C, D = data[1], data[2], data[3], data[4]
E, F, G, H = data[5], data[6], data[7], data[8]

solutions = []

for x in range(N + 1):
    c1 = B - C
    r1 = D - A * x - C * (N - x)
    
    possible1 = False
    y1 = -1
    
    if c1 == 0:
        if r1 == 0:
            possible1 = True
    else:
        if r1 % c1 == 0:
            y1 = r1 // c1

    c2 = F - G
    r2 = H - E * x - G * (N - x)
    
    possible2 = False
    y2 = -1
    
    if c2 == 0:
        if r2 == 0:
            possible2 = True
    else:
        if r2 % c2 == 0:
            y2 = r2 // c2

    if (c1 != 0 and y1 == -1) or (c2 != 0 and y2 == -1):
        continue
    
    if (c1 == 0 and not possible1) or (c2 == 0 and not possible2):
        continue

    valid_y = []
    
    start_y = 0
    end_y = N - x
    
    if possible1 and possible2:
        if end_y >= start_y:
            count = end_y - start_y + 1
            if count > 1 or len(solutions) > 0:
                print(1)
                sys.exit(0)
            valid_y.append(start_y)
    elif possible1 and not possible2:
        if start_y <= y2 <= end_y:
            valid_y.append(y2)
    elif not possible1 and possible2:
        if start_y <= y1 <= end_y:
            valid_y.append(y1)
    else:
        if y1 == y2 and start_y <= y1 <= end_y:
            valid_y.append(y1)
            
    for y in valid_y:
        solutions.append((x, y, N - x - y))
        if len(solutions) > 1:
            print(1)
            sys.exit(0)

if len(solutions) == 0:
    print(2)
elif len(solutions) == 1:
    print(0)
    print(*solutions[0])
else:
    print(1)