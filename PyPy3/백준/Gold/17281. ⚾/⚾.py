import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input().strip())
results = [list(map(int, input().split())) for _ in range(N)]

def simulate(order):
    score = 0
    batter_idx = 0  

    for inning in range(N):
        outs = 0
        b1 = b2 = b3 = 0 

        while outs < 3:
            player = order[batter_idx]      
            outcome = results[inning][player]
            batter_idx = (batter_idx + 1) % 9

            if outcome == 0:  # 아웃
                outs += 1
            elif outcome == 1:  
                score += b3
                b3, b2, b1 = b2, b1, 1
            elif outcome == 2:
                score += b3 + b2
                b3, b2, b1 = b1, 1, 0
            elif outcome == 3: 
                score += b3 + b2 + b1
                b3, b2, b1 = 1, 0, 0
            else:
                score += b3 + b2 + b1 + 1
                b1 = b2 = b3 = 0
    return score

best = 0
players = [i for i in range(1, 9)] 
for perm in permutations(players, 8):
    order = [0] * 9
    order[3] = 0  
    pi = 0
    for i in range(9):
        if i == 3:
            continue
        order[i] = perm[pi]
        pi += 1
    best = max(best, simulate(order))

print(best)