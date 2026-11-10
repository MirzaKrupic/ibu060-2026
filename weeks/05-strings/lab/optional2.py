sentence = input("Sentence: ")
words = []
for word in sentence.split():
    words.append(word[0].upper() + word[1:].lower())
print("Title:", " ".join(words))
