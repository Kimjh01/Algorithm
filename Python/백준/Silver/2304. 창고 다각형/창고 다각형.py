n = int(input())
cols = [tuple(map(int, input().split())) for _ in range(n)]
cols.sort()

pos = [c[0] for c in cols]
h   = [c[1] for c in cols]

max_h = max(h)
left_max = next(i for i, hh in enumerate(h) if hh == max_h)
right_max = len(h) - 1 - next(i for i, hh in enumerate(reversed(h)) if hh == max_h)

area = 0

area += max_h * (pos[right_max] - pos[left_max] + 1)

cur_h = h[0]
cur_x = pos[0]
for i in range(1, left_max + 1):
    if h[i] >= cur_h:
        area += (pos[i] - cur_x) * cur_h
        cur_h = h[i]
        cur_x = pos[i]

cur_h = h[-1]
cur_x = pos[-1]
for i in range(n - 2, right_max - 1, -1):
    if h[i] >= cur_h:
        area += (cur_x - pos[i]) * cur_h
        cur_h = h[i]
        cur_x = pos[i]

print(area)
