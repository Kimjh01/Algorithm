import sys
input = sys.stdin.readline

L = int(input().strip())

Arcanes = [200, 210, 220, 225, 230, 235, 245, 250]
Authentics = [260, 265, 270, 275, 280, 285, 290, 295, 300]

arc_res = []
for i in range(6):  
    if Arcanes[i+2] <= L:
        arc_res.append("100")
    elif Arcanes[i+1] <= L:
        arc_res.append("300")
    elif Arcanes[i] <= L:
        arc_res.append("500")
    else:
        arc_res.append("0")

auth_res = []
for i in range(7):  
    if Authentics[i+2] <= L:
        auth_res.append("100")
    elif Authentics[i+1] <= L:
        auth_res.append("300")
    elif Authentics[i] <= L:
        auth_res.append("500")
    else:
        auth_res.append("0")

print(" ".join(arc_res))
print(" ".join(auth_res))
