import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))

prefix = [0]*(N+1)
for i in range(1, N+1):
    prefix[i] = prefix[i-1] + arr[i-1]

val = 0 
for _ in range(M):
    a, b = map(int, input().split())
    val = prefix[b] - prefix[a-1]
    print(val)
    val = 0 