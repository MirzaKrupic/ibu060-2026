student = lambda price: price * 80 / 100
senior = lambda price: price * 70 / 100
regular = lambda price: price

kind = input("Customer: ")
price = int(input("Price: "))
if kind == "student":
    print("Price to pay:", student(price))
elif kind == "senior":
    print("Price to pay:", senior(price))
elif kind == "regular":
    print("Price to pay:", regular(price))
else:
    print("Unknown customer")
