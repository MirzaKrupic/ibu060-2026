def with_vat(price):
    return price + price * 20 / 100


price = int(input("Price: "))
print(with_vat(price))
