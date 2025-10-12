import sys
input = sys.stdin.readline

n, L = map(int, input().split())
max_blocks = 0
cnt_at_max = 0

for _ in range(n):
    s = input().strip()
    blocks = 0
    prev = '0'
    for ch in s:
        if prev == '0' and ch == '1':
            blocks += 1
        prev = ch

    if blocks > max_blocks:
        max_blocks = blocks
        cnt_at_max = 1
    elif blocks == max_blocks:
        cnt_at_max += 1

print(max_blocks, cnt_at_max)
