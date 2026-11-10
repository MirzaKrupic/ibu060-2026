def is_adult(age):
    return age >= 18


age = int(input("Age: "))
if is_adult(age):
    print("Adult")
else:
    print("Minor")
