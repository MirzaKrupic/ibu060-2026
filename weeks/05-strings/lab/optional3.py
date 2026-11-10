word = input("Word: ")
half = len(word) // 2
print("Swapped:", word[half:] + word[:half])
