N = int(input().strip())
F = int(input().strip())

base = (N // 100) * 100
add = (F - (base % F)) % F
print(f"{add:02d}")
