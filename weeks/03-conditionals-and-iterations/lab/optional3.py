count = int(input("How many: "))
first = int(input("Number: "))
smallest = first
largest = first
for i in range(count - 1):
    x = int(input("Number: "))
    if x < smallest:
        smallest = x
    if x > largest:
        largest = x
print("Smallest:", smallest)
print("Largest:", largest)
