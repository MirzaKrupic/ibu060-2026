s = int(input("Seconds: "))
h = s // 3600
m = s % 3600 // 60
sec = s % 60
print(s, "s =", h, "h", m, "min", sec, "s")
