N = int(input())
sizes = list(map(int, input().split()))
T, P = map(int, input().split())

T_total = 0   
for x in sizes:  
    buy_T = (x + T - 1) // T
    T_total += buy_T

Pen_total = N // P
Pen_total_alpha = N % P

print(T_total)
print(Pen_total, Pen_total_alpha)