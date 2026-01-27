import sys

input = sys.stdin.readline
n = int(input().strip())
pat = input().strip()
pre, suf = pat.split('*', 1)

out = []
lp = len(pre)
ls = len(suf)

for _ in range(n):
    s = input().strip()
    if len(s) < lp + ls:
        out.append("NE")
    else:
        if s[:lp] == pre and s[len(s) - ls:] == suf:
            out.append("DA")
        else:
            out.append("NE")

sys.stdout.write("\n".join(out))
