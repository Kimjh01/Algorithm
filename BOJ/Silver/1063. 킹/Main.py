import sys

input = sys.stdin.read
data = input().split()

k = data[0]
s = data[1]
n = int(data[2])

DIR = {
    "R": (1, 0),"L": (-1, 0),
    "B": (0, -1),"T": (0, 1),
    "RT": (1, 1),"LT": (-1, 1),
    "RB": (1, -1),"LB": (-1, -1),
}

x = ord(k[0]) - ord('A')
y = int(k[1]) - 1
sx = ord(s[0]) - ord('A')
sy = int(s[1]) - 1

for i in range(3, 3 + n):
    dx, dy = DIR[data[i]]
    nx, ny = x + dx, y + dy
    if 0 <= nx < 8 and 0 <= ny < 8:
        if nx == sx and ny == sy:
            tx, ty = sx + dx, sy + dy
            if 0 <= tx < 8 and 0 <= ty < 8:
                x, y = nx, ny
                sx, sy = tx, ty
        else:
            x, y = nx, ny

print(chr(x + ord('A')) + str(y + 1))
print(chr(sx + ord('A')) + str(sy + 1))
