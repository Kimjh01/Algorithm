import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
skills = list(map(int, input().split()))
dq = deque()

for i, s in enumerate(reversed(skills)):
    card = i + 1
    if s == 1:
        dq.appendleft(card)
    elif s == 2:
        dq.insert(1, card)
    else:
        dq.append(card)

print(*dq)