phrase = input("Phrase: ")
result = ""
for word in phrase.split():
    result += word[0].upper()
print("Acronym:", result)
