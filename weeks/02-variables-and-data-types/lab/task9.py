RATE = 2.50
minutes = int(input("Minutes parked: "))
hours = (minutes + 59) // 60
print("Hours charged:", hours)
print(f"Fee: {hours * RATE:.2f} KM")
