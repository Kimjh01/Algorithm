import sys

input = sys.stdin.readline
t = int(input().strip())
out = []
for _ in range(t):
    n, m = map(int, input().split())
    cars = {}
    for _ in range(n):
        name, cost, rent, per = input().split()
        cars[name] = (int(cost), int(rent), int(per))
    agents = {}
    for _ in range(m):
        time, aname, ev, detail = input().split()
        if aname not in agents:
            agents[aname] = [None, 0, False]
        cur, price, bad = agents[aname]
        if ev == 'p':
            if bad or cur is not None:
                agents[aname][2] = True
            else:
                if detail not in cars:
                    agents[aname][2] = True
                else:
                    agents[aname][0] = detail
                    agents[aname][1] = price + cars[detail][1]
        elif ev == 'r':
            if bad or cur is None:
                agents[aname][2] = True
            else:
                dist = int(detail)
                agents[aname][1] = price + cars[cur][2] * dist
                agents[aname][0] = None
        else:
            if bad or cur is None:
                agents[aname][2] = True
            else:
                perc = int(detail)
                cost = cars[cur][0]
                agents[aname][1] = price + (cost * perc + 99) // 100
    for name in sorted(agents.keys()):
        cur, price, bad = agents[name]
        if bad or cur is not None:
            out.append(f"{name} INCONSISTENT")
        else:
            out.append(f"{name} {price}")
sys.stdout.write("\n".join(out))
