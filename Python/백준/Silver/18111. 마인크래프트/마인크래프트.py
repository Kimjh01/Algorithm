import sys

data = list(map(int, sys.stdin.buffer.read().split()))
N, M, B = data[0], data[1], data[2]
vals = data[3:] 

cnt = [0]*257
min_h, max_h = 256, 0
for v in vals:
    cnt[v] += 1
    if v < min_h: min_h = v
    if v > max_h: max_h = v

pc = [0]*257
ps = [0]*257
pc[0] = cnt[0]
ps[0] = 0 * cnt[0]
for i in range(1, 257):
    pc[i] = pc[i-1] + cnt[i]
    ps[i] = ps[i-1] + i*cnt[i]

total = N*M
total_sum = ps[256]

best_time = 10**18
best_h = -1

for h in range(min_h, max_h+1):
    if h > 0:
        below_cnt = pc[h-1]
        below_sum = ps[h-1]
    else:
        below_cnt = 0
        below_sum = 0
    place = h*below_cnt - below_sum  

    above_cnt = total - pc[h]
    above_sum = total_sum - ps[h]
    remove = above_sum - h*above_cnt 

    inv = B + remove - place
    if inv < 0:
        continue 

    t = remove*2 + place
    if t < best_time or (t == best_time and h > best_h):
        best_time = t
        best_h = h

print(best_time, best_h)
