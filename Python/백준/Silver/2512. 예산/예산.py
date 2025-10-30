import sys
input = sys.stdin.readline

# 지방의 수
n = int(input())

# 각 지방의 예산요청 
requests = list(map(int, input().split()))

# 총 예산 
total = int(input())

# 만일 지방 예산 요청 총합이 총 예산보다 작으면 바로 나눠주고 치워버려
if sum(requests) <= total:
    print(max(requests))
    sys.exit(0)

# 이진탐새을 통해 적절한 값 찾기 
low, high = 0, max(requests)
ans = 0
while low <= high:

    # 각 지방의 예산 요청에 평균을 기준
    mid = (low + high) // 2  
    s = 0
    
    # 예산들을 하나씩 비교
    for r in requests:
        s += r if r <= mid else mid
    
    # 평균 또는 예산들의 합이 같지 않으면 범위 조정
    if s <= total:
        ans = mid     
        low = mid + 1
    else:
        high = mid - 1

print(ans)