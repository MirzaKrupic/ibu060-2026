guests = int(input("Guests: "))
per_guest = int(input("Slices per guest: "))
slices = guests * per_guest
pizzas = (slices + 7) // 8
print("Pizzas:", pizzas)
print("Slices left:", pizzas * 8 - slices)
