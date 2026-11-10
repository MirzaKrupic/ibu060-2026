w1 = input("Word 1: ")
w2 = input("Word 2: ")
w3 = input("Word 3: ")
w4 = input("Word 4: ")
words = [w1, w2, w3, w4]
long_words = list(filter(lambda w: len(w) > 5, words))
print("Long words:", len(long_words))
