count_revolvers, money = [int(x) for x in input().split()]
price_revolvers: list[int] = [int(x) for x in input().split()]

biggest_price: int = 0
for elem in price_revolvers:
    if biggest_price < elem <= money:
        biggest_price = elem

print(biggest_price)
