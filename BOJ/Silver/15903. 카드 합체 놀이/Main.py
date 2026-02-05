n, m = map(int, input().split())
cards = list(map(int, input().split()))
for _ in range(m):
    cards.sort()
    s = cards[0] + cards[1]
    cards[0] = cards[1] = s
print(sum(cards))