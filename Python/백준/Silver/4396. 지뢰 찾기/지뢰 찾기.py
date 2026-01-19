import sys
input = sys.stdin.readline

n = int(input())
mines = [list(input().strip()) for _ in range(n)]
board = [list(input().strip()) for _ in range(n)]
result = [['.'] * n for _ in range(n)]
game_over = False

for r in range(n):
    for c in range(n):
        if board[r][c] == 'x':
            if mines[r][c] == '*':
                game_over = True
            else:
                count = 0
                for dr in range(-1, 2):
                    for dc in range(-1, 2):
                        if dr == 0 and dc == 0:
                            continue
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n:
                            if mines[nr][nc] == '*':
                                count += 1
                result[r][c] = str(count)

if game_over:
    for r in range(n):
        for c in range(n):
            if mines[r][c] == '*':
                result[r][c] = '*'

for row in result:
    print("".join(row))