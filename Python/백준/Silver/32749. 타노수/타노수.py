import sys
input = sys.stdin.readline

N, T = map(int, input().split())
number = input().strip()  

seg_len = 1 << (N - T)

ans = ""
for i in range(0, len(number), seg_len):
    seg = number[i:i + seg_len]
    if seg > ans:
        ans = seg

print(ans)
