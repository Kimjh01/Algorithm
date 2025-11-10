import sys

doc = sys.stdin.readline().rstrip('\n')
word = sys.stdin.readline().rstrip('\n')

ld, lw = len(doc), len(word)
cnt = 0
i = 0

while i <= ld - lw:
    if doc[i:i+lw] == word:
        cnt += 1
        i += lw  
    else:
        i += 1

print(cnt)
