import sys
input = sys.stdin.readline

N = int(input().strip())
shift_hours = [4, 6, 4, 10]

work_time = {}
for _ in range(N):
    for shift in range(4):
        names = input().split()
        hours = shift_hours[shift]
        for name in names:
            if name == '-':
                continue
            if name not in work_time:
                work_time[name] = 0
            work_time[name] += hours

if not work_time:
    print("Yes")
else:
    max_time = max(work_time.values())
    min_time = min(work_time.values())
    if max_time - min_time <= 12:
        print("Yes")
    else:
        print("No")
        