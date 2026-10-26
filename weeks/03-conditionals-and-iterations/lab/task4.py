count = int(input("How many: "))
total = 0
for i in range(count):
    score = int(input("Score: "))
    total += score
print("Average:", total / count)
