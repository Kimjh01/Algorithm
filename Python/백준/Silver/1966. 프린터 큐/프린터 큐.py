from collections import deque

t = int(input())
for case in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    q = deque([])
    for j in range(n):
        q.append((j, arr[j]))  

    arr = sorted(arr, reverse=True)
    cnt = 0
    idx_sorted = 0

    while q:
        idx, val = q.popleft()
        if val == arr[idx_sorted]:
            cnt += 1
            idx_sorted += 1
            if idx == m:
                print(cnt)
                break
        else:
            q.append((idx, val))