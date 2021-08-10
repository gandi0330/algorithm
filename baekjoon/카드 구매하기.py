card = int(input())

cardpack = list(map(int,input().split()))

onecard_price = {price / (idx+1) : idx+1 for idx, price in enumerate(cardpack)}

sum_price = 0
while True:

    high_price_card = max(sorted(onecard_price.keys(), reverse=True))
    cards = onecard_price[high_price_card]

    if cards <= card:
        card -= cards
        sum_price += high_price_card * cards
    
    else :
        del onecard_price[high_price_card]
    
    if card == 0 :
        break

print(int(sum_price))