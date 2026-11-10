def shipping(weight, express=False):
    cost = 5 + 2 * weight
    if express:
        cost += 10
    return cost


weight = int(input("Weight (kg): "))
print("Standard:", shipping(weight))
print("Express:", shipping(weight, True))
