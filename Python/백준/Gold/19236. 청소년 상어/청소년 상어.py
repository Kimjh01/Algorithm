import sys
input = sys.stdin.readline

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

board = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        fish_num = data[2 * j]
        fish_dir = data[2 * j + 1] - 1
        board[i][j] = [fish_num, fish_dir]  

answer = 0

def move_fishes(board, shark_x, shark_y):
    for fn in range(1, 17):
        fx = fy = -1
        fd = -1
        exist = False

        for x in range(4):
            for y in range(4):
                if board[x][y][0] == fn:
                    fx, fy = x, y
                    fd = board[x][y][1]
                    exist = True
                    break
            if exist:
                break

        if not exist:
            continue  

        for rot in range(8):
            nd = (fd + rot) % 8
            nx = fx + dx[nd]
            ny = fy + dy[nd]

            if not (0 <= nx < 4 and 0 <= ny < 4):
                continue
            if nx == shark_x and ny == shark_y:
                continue

            board[fx][fy][1] = nd
            board[fx][fy], board[nx][ny] = board[nx][ny], board[fx][fy]
            break


def dfs(board, sx, sy, sdir, total):
    global answer

    move_fishes(board, sx, sy)

    can_move = False
    for step in range(1, 4):
        nx = sx + dx[sdir] * step
        ny = sy + dy[sdir] * step

        if not (0 <= nx < 4 and 0 <= ny < 4):
            break
        if board[nx][ny][0] == 0:
            continue  

        can_move = True
        new_board = [[cell[:] for cell in row] for row in board]
        fish_num, fish_dir = new_board[nx][ny]
        new_board[sx][sy] = [0, 0]
        new_board[nx][ny] = [0, 0]

        dfs(new_board, nx, ny, fish_dir, total + fish_num)

    if not can_move:
        answer = max(answer, total)


first_num, first_dir = board[0][0]
board[0][0] = [0, 0] 

dfs(board, 0, 0, first_dir, first_num)

print(answer)
