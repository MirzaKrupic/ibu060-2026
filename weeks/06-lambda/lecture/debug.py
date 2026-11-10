adult = lambda age: "Yes" if age >= 18 else "No"
print(adult(18))

volume = lambda w, h, d: w * h * d
print(volume(2, 3, 4))

big = list(filter(lambda n: n > 2, [1, 2, 3, 4]))
print(len(big))

sign = lambda n: "Plus" if n > 0 else "Minus"
print(sign(5))
