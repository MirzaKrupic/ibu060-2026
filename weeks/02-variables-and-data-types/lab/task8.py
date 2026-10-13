distance = float(input("Distance (km): "))
consumption = float(input("Consumption (l/100 km): "))
price = float(input("Price per litre: "))
litres = distance * consumption / 100
cost = litres * price
print(f"Fuel needed: {litres:.2f} l")
print(f"Trip cost: {cost:.2f} KM")
