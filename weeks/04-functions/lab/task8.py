def line_total(price, quantity):
    return price * quantity


def receipt_total(price1, quantity1, price2, quantity2):
    return line_total(price1, quantity1) + line_total(price2, quantity2)


price1 = int(input("Price 1: "))
quantity1 = int(input("Quantity 1: "))
price2 = int(input("Price 2: "))
quantity2 = int(input("Quantity 2: "))
print("Item 1:", line_total(price1, quantity1))
print("Item 2:", line_total(price2, quantity2))
print("Total:", receipt_total(price1, quantity1, price2, quantity2))
