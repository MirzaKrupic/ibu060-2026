delivery = lambda total: "Free" if total >= 50 else "Paid"

total = int(input("Total: "))
print("Delivery:", delivery(total))
