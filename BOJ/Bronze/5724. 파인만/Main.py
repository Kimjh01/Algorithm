import sys

out = []
while True:
    line = sys.stdin.readline()
    if not line:
        break
    n = int(line.strip())
    if n == 0:
        break
    out.append(str(n * (n + 1) * (2 * n + 1) // 6))
sys.stdout.write("\n".join(out))
