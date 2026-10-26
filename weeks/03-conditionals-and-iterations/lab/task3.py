speed = int(input("Wind speed: "))
if speed < 20:
    print("Calm")
elif speed < 50:
    print("Breezy")
elif speed < 90:
    print("Strong wind")
else:
    print("Storm")
