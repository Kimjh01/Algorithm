import sys
input = sys.stdin.readline

A, B = map(int, input().split())

start = max(4, A)
end = B

if start % 2 != 0:
    start += 1
if end % 2 != 0:
    end -= 1

if start > end:
    print(0)
else:
    count = (end - start) // 2 + 1
    total = (start + end) * count // 2
    print(total)