import sys
input = sys.stdin.readline

while True:
    line = input().split()
    if not line:
        break
    b, n = map(int, line)
    if b == 0 and n == 0:
        break

    a = 1
    while True:
        val = a ** n
        if val >= b:
            break
        a += 1

    prev_val = (a - 1) ** n
    curr_val = a ** n

    if abs(b - prev_val) <= abs(b - curr_val):
        print(a - 1)
    else:
        print(a)
