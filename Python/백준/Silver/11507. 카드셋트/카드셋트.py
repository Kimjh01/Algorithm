import sys
s = sys.stdin.readline().strip()
cards = [s[i:i+3] for i in range(0, len(s), 3)]

if len(cards) != len(set(cards)):
    print("GRESKA")
else:
    p, k, h, t = 13, 13, 13, 13
    for card in cards:
        if card[0] == 'P': p -= 1
        elif card[0] == 'K': k -= 1
        elif card[0] == 'H': h -= 1
        elif card[0] == 'T': t -= 1
    print(p, k, h, t)