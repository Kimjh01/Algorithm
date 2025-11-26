buttons = list(map(int, input().split()))
money = 5000
cost = {1: 500, 2: 800, 3: 1000}

for b in buttons:
    money -= cost[b]

print(money)
