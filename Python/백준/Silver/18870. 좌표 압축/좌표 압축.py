n = int(input())
nums = list(map(int, input().split()))
arr = sorted(set(nums))
rank = {v: i for i, v in enumerate(arr)}
print(' '.join(str(rank[x]) for x in nums))