import sys
input = sys.stdin.readline
N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x: (x[1], x[0]))
cnt = 0
end = 0
for s, e in arr:
    if s >= end:  
        cnt += 1
        end = e
print(cnt)