N = int(input().strip())
nums = [int(input().strip()) for _ in range(N)]
nums.sort()
print("\n".join(map(str, nums)))
