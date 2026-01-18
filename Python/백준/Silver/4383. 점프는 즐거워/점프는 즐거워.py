import sys

for line in sys.stdin:
    try:
        parts = list(map(int, line.split()))
        if not parts:
            continue
        
        n = parts[0]
        nums = parts[1:]
        
        if n == 1:
            print("Jolly")
            continue
        
        diffs = set()
        for i in range(n - 1):
            d = abs(nums[i] - nums[i+1])
            if 0 < d < n:
                diffs.add(d)
        
        if len(diffs) == n - 1:
            print("Jolly")
        else:
            print("Not jolly")
    except:
        break