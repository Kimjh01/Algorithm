import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    rs = [0] * (n + 1)  # 득점
    ra = [0] * (n + 1)  # 실점
    for _ in range(m):
        a, b, p, q = map(int, input().split())
        rs[a] += p; ra[a] += q
        rs[b] += q; ra[b] += p
    best = -1.0
    worst = 1e9
    for i in range(1, n + 1):
        num = rs[i] * rs[i] + ra[i] * ra[i]
        e = 0.0 if num == 0 else (rs[i] * rs[i]) / num
        if e > best: best = e
        if e < worst: worst = e
    print(int(best * 1000))
    print(int(worst * 1000))
