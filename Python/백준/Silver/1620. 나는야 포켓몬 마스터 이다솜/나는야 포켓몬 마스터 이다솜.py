import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = ["" for _ in range(N)]
idx = {}

for i in range(N):
    name = input().strip()
    arr[i] = name      
    idx[name] = i + 1   

out = []
for _ in range(M):
    q = input().strip()
    if q.isdigit():        
        out.append(arr[int(q) - 1])
    else:                  
        out.append(str(idx[q]))

print("\n".join(out))
