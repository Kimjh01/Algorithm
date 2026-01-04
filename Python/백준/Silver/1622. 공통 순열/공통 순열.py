import sys

lines = sys.stdin.read().splitlines()

for i in range(0, len(lines), 2):
    if i + 1 >= len(lines): break
    a = lines[i]
    b = lines[i+1]
    
    result = ""
    for char in "abcdefghijklmnopqrstuvwxyz":
        count = min(a.count(char), b.count(char))
        result += char * count
    
    print(result)