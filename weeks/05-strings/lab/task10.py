password = input("Password: ")
has_digit = False
for ch in password:
    if ch in "0123456789":
        has_digit = True
long_enough = len(password) >= 8
if long_enough:
    print("Length: ok")
else:
    print("Length: too short")
if has_digit:
    print("Digit: ok")
else:
    print("Digit: missing")
if long_enough and has_digit:
    print("Result: Strong")
else:
    print("Result: Weak")
