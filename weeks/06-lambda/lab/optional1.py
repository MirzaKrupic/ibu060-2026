initials = lambda first, last: first[0].upper() + last[0].upper()

first = input("First name: ")
last = input("Last name: ")
print("Initials:", initials(first, last))
