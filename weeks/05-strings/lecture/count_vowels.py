word = input("Enter a word: ").lower()
count = 0
for letter in word:
    if letter in "aeiou":
        count += 1
print("Vowels:", count)
