import sys

input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1

for _ in range(t):
    n = int(data[idx])
    idx += 1
    current_nums = []
    for _ in range(n):
        current_nums.append(int(data[idx]))
        idx += 1
    print(min(current_nums), max(current_nums))