import sys
from collections import deque

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    P = input().strip()
    n = int(input())
    s = input().strip()

    if s == "[]":
        arr = deque()
    else:
        arr = deque(map(int, s[1:-1].split(',')))

    reversed_flag = False
    error = False

    for cmd in P:
        if cmd == 'R':
            reversed_flag = not reversed_flag
        else: 
            if not arr:
                print("error")
                error = True
                break
            if reversed_flag:
                arr.pop()
            else:
                arr.popleft()

    if error:
        continue

    if reversed_flag:
        arr.reverse()

    print("[" + ",".join(map(str, arr)) + "]")