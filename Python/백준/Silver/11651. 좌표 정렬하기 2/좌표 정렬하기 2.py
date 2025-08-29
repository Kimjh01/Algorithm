import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]  

arr.sort(key=lambda p: (p[1], p[0])) 

out_lines = [f"{x} {y}" for x, y in arr]
sys.stdout.write("\n".join(out_lines))