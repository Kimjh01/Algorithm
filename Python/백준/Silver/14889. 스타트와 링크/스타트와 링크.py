import sys
from itertools import combinations

input = sys.stdin.readline
N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]

members = list(range(N))
min_val = float('inf')

"""
for s_team in combinations(members[1:], N//2 - 1):
    s_team = (0,) + s_team
"""

for s_team in combinations(members, N // 2):    
    s_set = set(s_team)
    l_team = [x for x in members if x not in s_set]
    s_score = 0
    l_score = 0
    
    for i in range(N // 2):
        for j in range(i + 1, N // 2):
            
            s1, s2 = s_team[i], s_team[j]
            s_score += S[s1][s2] + S[s2][s1]

            l1, l2 = l_team[i], l_team[j]
            l_score += S[l1][l2] + S[l2][l1]


    val = abs(s_score - l_score)
    
    if val < min_val:
        min_val = val
        
    if min_val == 0:
        break
        
print(min_val)