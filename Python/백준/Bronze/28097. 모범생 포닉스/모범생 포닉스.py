N = int(input())
time = list(map(int, input().split()))
total = sum(time) + (N-1)*8
print(total//24, total%24)