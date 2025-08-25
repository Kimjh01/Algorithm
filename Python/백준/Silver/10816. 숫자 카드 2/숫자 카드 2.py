from collections import Counter
N = int(input())
arr = list(map(int, input().split()))
M = int(input())
ck = list(map(int, input().split()))
freq = Counter(arr)
print(" ".join(str(freq[x]) for x in ck))