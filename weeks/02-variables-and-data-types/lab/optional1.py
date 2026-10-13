amount = float(input("Amount: "))
years = int(input("Years: "))
final = amount * (1 + 0.03) ** years
print(f"After {years} years: {final:,.2f} KM")
