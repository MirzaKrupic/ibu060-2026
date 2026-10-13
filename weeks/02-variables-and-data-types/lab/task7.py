n = int(input("Number: "))
hundreds = n // 100
tens = n // 10 % 10
ones = n % 10
reversed_n = ones * 100 + tens * 10 + hundreds
print(n, "reversed is", reversed_n)
