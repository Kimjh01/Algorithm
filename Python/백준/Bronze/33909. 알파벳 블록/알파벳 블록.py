import sys
input = sys.stdin.readline

S, C, O, N = map(int, input().split())
total_sn = S + N
total_c_val = C + (O * 2)
ans = min(total_sn // 3, total_c_val // 6)

print(ans)