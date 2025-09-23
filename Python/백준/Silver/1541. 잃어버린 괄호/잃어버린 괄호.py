import sys
s = sys.stdin.readline().strip()
parts = s.split('-')
def sum_group(token: str) -> int:
    return sum(map(int, token.split('+'))) if token else 0
ans = sum_group(parts[0])
for t in parts[1:]:
    ans -= sum_group(t)
print(ans)