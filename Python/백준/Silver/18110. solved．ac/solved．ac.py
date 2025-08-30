import sys
input = sys.stdin.readline
n = int(input())
if n == 0:
    print(0)
else:
    scores = [int(input()) for _ in range(n)]
    scores.sort()
    k = int(n * 0.15 + 0.5)
    if k > 0:
        ans = scores[k:n-k]
    else:
        ans = scores
    avg = sum(ans) / len(ans)
    print(int(avg + 0.5))
