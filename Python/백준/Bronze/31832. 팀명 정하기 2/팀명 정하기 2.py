import sys

def ok(s):
    upp = sum(c.isupper() for c in s)
    low = sum(c.islower() for c in s)
    if not (low >= upp): 
        return False
    if len(s) > 10: 
        return False
    if all(c.isdigit() for c in s): 
        return False
    return True

input = sys.stdin.readline
n = int(input())
for _ in range(n):
    s = input().strip()
    if ok(s):
        print(s)
        break