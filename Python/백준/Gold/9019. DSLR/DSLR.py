import sys
from collections import deque
input = sys.stdin.readline

MAX = 10000
D = [0]*MAX
S = [0]*MAX
L = [0]*MAX
R = [0]*MAX
for x in range(MAX):
    D[x] = (x * 2) % 10000
    S[x] = 9999 if x == 0 else x - 1
    L[x] = ((x % 1000) * 10) + (x // 1000)
    R[x] = ((x % 10) * 1000) + (x // 10)

visited = [0] * MAX     
parent  = [-1] * MAX
how     = bytearray(MAX) 
run_id = 0

def bfs(a, b):
    global run_id
    run_id += 1

    q = deque()
    q.append(a)
    visited[a] = run_id
    parent[a] = -1
    vis = visited
    par = parent
    op  = how
    rid = run_id
    q_popleft = q.popleft
    q_append = q.append

    while q:
        x = q_popleft()
        if x == b:
            break

        nx = D[x]
        if vis[nx] != rid:
            vis[nx] = rid; par[nx] = x; op[nx] = ord('D'); q_append(nx)
            if nx == b: break

        nx = S[x]
        if vis[nx] != rid:
            vis[nx] = rid; par[nx] = x; op[nx] = ord('S'); q_append(nx)
            if nx == b: break

        nx = L[x]
        if vis[nx] != rid:
            vis[nx] = rid; par[nx] = x; op[nx] = ord('L'); q_append(nx)
            if nx == b: break

        nx = R[x]
        if vis[nx] != rid:
            vis[nx] = rid; par[nx] = x; op[nx] = ord('R'); q_append(nx)

    res = []
    cur = b
    while cur != a:
        res.append(chr(op[cur]))
        cur = par[cur]
    res.reverse()
    return ''.join(res)

T = int(input())
out = []
for _ in range(T):
    a, b = map(int, input().split())
    out.append(bfs(a, b))
print('\n'.join(out))
