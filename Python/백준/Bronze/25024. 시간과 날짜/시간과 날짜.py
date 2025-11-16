T = int(input())

for _ in range(T):
    x, y = map(int, input().split())

    if 0 <= x <= 23 and 0 <= y <= 59:
        time_ok = "Yes"
    else:
        time_ok = "No"
        
    date_ok = "No"
    if 1 <= x <= 12:
        if x in [1, 3, 5, 7, 8, 10, 12]:
            if 1 <= y <= 31:
                date_ok = "Yes"

        elif x in [4, 6, 9, 11]:
            if 1 <= y <= 30:
                date_ok = "Yes"

        elif x == 2:
            if 1 <= y <= 29:
                date_ok = "Yes"

    print(time_ok, date_ok)
