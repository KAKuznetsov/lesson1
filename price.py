price = 100
discount = 500

def discounted (price, discount, max_discount = 20):
    price = abs(price)
    discount = abs(discount)
    max_discount = abs(max_discount)
    if max_discount >= 100:
        raise ValueError ("Максимальная скидка не должна быть больше 100 ")
    if discount >= max_discount:
        price_with_discount = price

    else:

        price_with_discount = price - (price * discount/ 100)
    return price_with_discount

discounted (price, discount)
discounted (-100, 50)
discounted (-100, -50)

price_disc = discounted (price, discount)
print(price_disc)
print(discounted (100, 50))
print(discounted (100, 100, max_discount = 500))

print ("Hello, world!")