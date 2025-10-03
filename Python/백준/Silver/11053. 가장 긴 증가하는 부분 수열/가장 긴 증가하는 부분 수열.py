import sys, bisect
input = sys.stdin.readline

N = int(input().strip())
a = list(map(int, input().split()))

tails = []
for x in a:
    i = bisect.bisect_left(tails, x) 
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
print(len(tails))
