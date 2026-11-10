def coins_needed(amount, coin=2):
    return amount // coin


amount = int(input("Amount: "))
print("Coins of 2:", coins_needed(amount))
print("Coins of 5:", coins_needed(amount, 5))
