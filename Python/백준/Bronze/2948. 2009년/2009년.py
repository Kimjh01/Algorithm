D, M = map(int, input().split())
mdays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = D - 1 + sum(mdays[:M])
week = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
print(week[days % 7])