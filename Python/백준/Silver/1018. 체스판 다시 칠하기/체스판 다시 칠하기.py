N, M = map(int, input().split())
board = [input().rstrip() for _ in range(N)]

min_repaint = float('inf')

for i in range(N - 7):
    for j in range(M - 7):
        cnt_w_start = 0  
        cnt_b_start = 0  
        for y in range(8):
            for x in range(8):
                cur = board[i+y][j+x]
                if (y + x) % 2 == 0:
                    if cur != 'W': cnt_w_start += 1
                    if cur != 'B': cnt_b_start += 1
                else:
                    if cur != 'B': cnt_w_start += 1
                    if cur != 'W': cnt_b_start += 1
        min_repaint = min(min_repaint, cnt_w_start, cnt_b_start)

print(min_repaint)
