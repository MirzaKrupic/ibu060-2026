word1 = input("Word 1: ")
word2 = input("Word 2: ")
word3 = input("Word 3: ")
words = [word1, word2, word3]
print("Longest:", max(words, key=lambda w: len(w)))
print("Shortest:", min(words, key=lambda w: len(w)))
