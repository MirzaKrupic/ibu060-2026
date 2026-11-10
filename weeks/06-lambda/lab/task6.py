speed_word = lambda v: "Slow" if v < 50 else ("Normal" if v < 90 else "Fast")

v = int(input("Speed: "))
print("Speed:", speed_word(v))
