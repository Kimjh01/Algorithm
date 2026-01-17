import sys
input = sys.stdin.readline

N = int(input())
scores = [0] * (N + 1)

for _ in range(N * (N - 1) // 2):
    a, b, sa, sb = map(int, input().split())
    if sa > sb:
        scores[a] += 3
    elif sa < sb:
        scores[b] += 3
    else:
        scores[a] += 1
        scores[b] += 1

for i in range(1, N + 1):
    rank = 1
    for j in range(1, N + 1):
        if scores[j] > scores[i]:
            rank += 1
    print(rank)