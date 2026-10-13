bill = float(input("Bill: "))
people = int(input("People: "))
tip_percent = int(input("Tip %: "))
tip = bill * tip_percent / 100
total = bill + tip
print(f"Tip: {tip:.2f} KM")
print(f"Total: {total:.2f} KM")
print(f"Each pays: {total / people:.2f} KM")
