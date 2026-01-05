import sys

def solve():
    input = sys.stdin.readline
    T = int(input().strip())
    out = []
    for _ in range(T):
        n, k = map(int, input().split())

        if k != 1:
            out.append(" ".join(map(str, range(1, n + 1))))
            continue

        if n <= 3:
            out.append("-1")
            continue

        hi = n // 2 + 1
        lo = 1
        ans = []
        while hi <= n and lo <= n // 2:
            ans.append(str(hi))
            ans.append(str(lo))
            hi += 1
            lo += 1

        if n % 2 == 1:
            ans.append(str(n)) 

        out.append(" ".join(ans))

    print("\n".join(out))

if __name__ == "__main__":
    solve()
