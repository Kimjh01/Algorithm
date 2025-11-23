import sys
input = sys.stdin.readline

R, C = map(int, input().split())
A, B = map(int, input().split())

rows = []

for i in range(R * A):
    row_chars = []
    for j in range(C * B):
        if ((i // A) + (j // B)) % 2 == 0:
            row_chars.append('X')
        else:
            row_chars.append('.')
    rows.append(''.join(row_chars))

print('\n'.join(rows))
