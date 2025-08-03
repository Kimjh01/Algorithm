t = int(input().strip())
for _ in range(t):
    s = input().strip()
    result = 0
    for seg in s.split('X'):
        n = len(seg)
        result += n * (n + 1) // 2
    print(result)
