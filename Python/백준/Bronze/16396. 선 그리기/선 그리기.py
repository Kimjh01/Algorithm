import sys
input = sys.stdin.readline

n = int(input())
segs = [tuple(map(int, input().split())) for _ in range(n)]
segs.sort()
ans = 0
if segs:
    cur_l, cur_r = segs[0]
    for l, r in segs[1:]:
        if r < l: l, r = r, l
        if l > cur_r:              
            ans += cur_r - cur_l
            cur_l, cur_r = l, r
        else:                        
            cur_r = max(cur_r, r)
    ans += cur_r - cur_l
print(ans)

