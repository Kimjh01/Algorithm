import sys
from collections import Counter
input = sys.stdin.readline
N = int(input())
arr = [int(input()) for _ in range(N)]

print(round(sum(arr) / N))

arr.sort()
print(arr[N // 2])

cnt = Counter(arr).most_common() 
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0]) 
else:
    print(cnt[0][0])

print(max(arr) - min(arr))