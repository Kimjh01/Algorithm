s = open(0).read().splitlines()

foods = []
queries = []
for line in s:
    if not line.strip():
        continue
    p = line.split()
    cmd = p[0]
    t = int(p[1])
    if cmd == "Query":
        queries.append(t)
    else:
        n = float(p[2])
        foods.append((cmd, t, n))

queries.sort()

out = []
for T in queries:
    r = 0.0
    for cmd, t, n in foods:
        if T < t:
            continue
        dt = T - t
        if cmd == "Chocolate":
            v = 8.0 * n - dt / 12.0
        else:
            v = 2.0 * n - (dt * dt) / 79.0
        if v > 0:
            r += v
    if r < 1.0:
        r = 1.0
    out.append(f"{T} {r:.1f}")

print("\n".join(out))
