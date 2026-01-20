import sys
input = sys.stdin.readline

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

ans = [0, 0, 0]  # -1,0,1

stack = [(0, 0, n)]
while stack:
    x, y, s = stack.pop()
    first = a[x][y]
    same = True

    for i in range(x, x + s):
        row = a[i]
        for j in range(y, y + s):
            if row[j] != first:
                same = False
                break
        if not same:
            break

    if same:
        ans[first + 1] += 1
    else:
        ns = s // 3
        for dx in (0, ns, 2 * ns):
            for dy in (0, ns, 2 * ns):
                stack.append((x + dx, y + dy, ns))

print(ans[0])
print(ans[1])
print(ans[2])