n = int(input())
board = [input() for _ in range(n)]
is_sator = True
for i in range(n):
    for j in range(n):
        if board[i][j] != board[j][i]:
            is_sator = False
            break
    if not is_sator:
        break
print("YES" if is_sator else "NO")