sentence = input("Sentence: ")
word = input("Word: ")
print("Censored:", sentence.replace(word, "***"))
print("Removed:", sentence.count(word))
