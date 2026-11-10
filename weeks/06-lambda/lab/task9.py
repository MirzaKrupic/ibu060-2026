score1 = int(input("Score 1: "))
score2 = int(input("Score 2: "))
score3 = int(input("Score 3: "))
scores = [score1, score2, score3]
print("With bonus:", list(map(lambda s: s + 5, scores)))
print("Passing:", list(filter(lambda s: s >= 50, scores)))
