import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T + 1):
    N = int(input())
    price_list = list(map(int, input().split()))
    price_list.sort() 

    discounted = []

    while price_list:
        price = price_list.pop() 
        original = round(price * 0.75) 

        if original in price_list:
            discounted.append(original)
            price_list.remove(original)

    discounted.sort() 
    print(f"Case #{t}:", *discounted)
