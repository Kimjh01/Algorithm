import sys
from itertools import permutations

input = sys.stdin.readline

N = int(input().strip())

match = []
for _ in range(N):
    match.append(list(map(int, input().split())))

players = list(range(1, 9))  

def try_game(order):
    score = 0
    batter = 0  

    for inning in range(N):
        outs = 0
        bases = 0  

        while outs < 3:
            p = order[batter]
            batter += 1
            if batter == 9:
                batter = 0

            r = match[inning][p]

            if r == 0:
                outs += 1
            elif r == 4:
                score += bases.bit_count() + 1
                bases = 0
            else:
                nxt_base = bases << r
                score += (nxt_base >> 3).bit_count()
                bases = nxt_base & 7
                bases |= 1 << (r - 1)

    return score

ans = 0

for perm in permutations(players, 8):
    order = [0] * 9
    order[3] = 0 

    pi = 0
    for pos in range(9):
        if pos == 3:
            continue
        order[pos] = perm[pi]
        pi += 1

    s = try_game(order)
    if s > ans:
        ans = s

print(ans)