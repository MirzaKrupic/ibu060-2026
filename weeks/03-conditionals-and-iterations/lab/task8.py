count = 0
total = 0
price = int(input("Price: "))
while price != 0:
    count += 1
    total += price
    price = int(input("Price: "))
print("Items:", count)
print("Total:", total)
