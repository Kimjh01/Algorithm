T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    floor = (N - 1) % H + 1
    room  = (N - 1) // H + 1
    print(floor * 100 + room)