g = 1
out = []

while True:
    n = int(input())
    if n == 0:
        break

    names = []
    nasty = []

    for i in range(n):
        parts = input().split()
        names.append(parts[0])
        for j in range(1, n):
            if parts[j] == 'N':
                sender = (i - j) % n
                nasty.append((sender, i))

    out.append(f"Group {g}")
    if not nasty:
        out.append("Nobody was nasty")
    else:
        for s, t in nasty:
            out.append(f"{names[s]} was nasty about {names[t]}")
    out.append("")
    g += 1

print("\n".join(out))
