import sys
input = sys.stdin.readline

n = int(input())
s = str(5 ** n)
pad = n - len(s)
print("0." + "0" * pad + s)