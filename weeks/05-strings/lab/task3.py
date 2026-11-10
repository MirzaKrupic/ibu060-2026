text = input("Text: ")
count = 0
for ch in text:
    if ch in "0123456789":
        count += 1
print("Digits:", count)
