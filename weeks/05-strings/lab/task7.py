word = input("Word: ").lower()
letter = input("Letter: ").lower()
count = 0
for ch in word:
    if ch == letter:
        count += 1
print("Count:", count)
